"""
Ingestion pipeline: memuat dokumen sumber (markdown/txt/pdf/docx + gambar di
dalamnya), memecahnya jadi chunk, dan menandai setiap chunk dengan metadata
versi (v2.0 aktif vs v1.4 arsip nonaktif) sehingga retrieval bisa memfilter
atau memberi peringatan konflik.

Desain ini disesuaikan dengan struktur ASLI
`nusantaracare_panduan_operasional_internal_v2.md` setelah ditelaah:

1. Dokumen punya YAML frontmatter berisi metadata resmi tingkat dokumen
   (doc_id, doc_title, doc_version, effective_date, is_active, owner).
   Ini dipakai sebagai nilai DEFAULT untuk semua chunk.
2. Hanya SATU subsection yang benar-benar arsip nonaktif, ditandai eksplisit
   di judulnya: "### Arsip Kebijakan v1.4 — NONAKTIF". Subsection lain yang
   menyebut "v1.4" dalam teksnya (mis. "Riwayat Perubahan dan Arsip
   Kebijakan", "Pengganti Aktif v2.0") adalah narasi AKTIF yang menjelaskan
   riwayat/pengganti — BUKAN bagian yang nonaktif. Karena itu deteksi versi
   di bawah HANYA mencocokkan kata "NONAKTIF" pada JUDUL section (bukan
   pada isi/body), plus metadata inline eksplisit `is_active: false` yang
   memang dituliskan penulis dokumen di dalam teks arsip tersebut, sebagai
   pengaman kedua.
3. Section FAQ (judul diawali "Pertanyaan", berisi banyak blok "**T: ... J:
   ...**") di-chunk PER PASANGAN tanya-jawab, bukan dipotong berdasarkan
   jumlah karakter — supaya satu jawaban tidak pernah terpotong di tengah.
4. Section lain di-chunk per-paragraf, dikemas hingga mendekati CHUNK_SIZE,
   supaya batas chunk selalu jatuh di batas paragraf (bukan memotong
   kalimat di tengah).
"""
from __future__ import annotations

import base64
import re
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from app.services import llm

# --- Konfigurasi chunking -----------------------------------------------
# ~900 karakter per chunk (di luar mode FAQ per-Q&A): cukup besar untuk
# menjaga satu ketentuan SOP/paragraf utuh dalam satu chunk (paragraf di
# dokumen ini rata-rata 400-900 karakter dan masing-masing membahas satu
# aturan/kondisi spesifik), cukup kecil agar top-k retrieval tetap presisi.
# Overlap 120 karakter hanya dipakai sebagai fallback saat SATU paragraf
# melebihi CHUNK_SIZE (jarang terjadi di dokumen ini).
CHUNK_SIZE = 900
CHUNK_OVERLAP = 120

_ACTIVE_VERSION_LABEL_FALLBACK = "2.0"

# --- Deteksi versi arsip (title-based, sesuai konvensi dokumen ini) ------
_NONAKTIF_IN_TITLE = re.compile(r"nonaktif", re.I)
_VERSION_IN_TITLE = re.compile(r"\bv?(\d+\.\d+)\b")
_INLINE_INACTIVE_META = re.compile(r"is_active:\s*`?false`?", re.I)


@dataclass
class SourceChunk:
    chunk_id: str
    text: str
    section_title: str
    doc_version: str
    is_active: bool
    modality: str = "text"  # "text" | "image"
    extra: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Loaders multi-format
# ---------------------------------------------------------------------------

def _read_markdown_or_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def _read_pdf(path: Path) -> str:
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    return "\n\n".join(page.extract_text() or "" for page in reader.pages)


def _read_docx(path: Path) -> str:
    import docx

    document = docx.Document(str(path))
    return "\n\n".join(p.text for p in document.paragraphs)


def load_raw_text(path: Path) -> str:
    """Router loader multi-format (memenuhi 'bisa menerima apa aja, ga harus md')."""
    suffix = path.suffix.lower()
    if suffix in (".md", ".markdown", ".txt"):
        return _read_markdown_or_text(path)
    if suffix == ".pdf":
        return _read_pdf(path)
    if suffix == ".docx":
        return _read_docx(path)
    raise ValueError(f"Format dokumen belum didukung: {suffix}")


def _extract_frontmatter(raw_text: str) -> tuple[dict[str, Any], str]:
    """Pisahkan YAML frontmatter (--- ... ---) dari body markdown, jika ada."""
    if raw_text.startswith("---"):
        end = raw_text.find("\n---", 3)
        if end != -1:
            fm_text = raw_text[3:end].strip()
            body = raw_text[end + 4:]
            try:
                meta = yaml.safe_load(fm_text) or {}
            except yaml.YAMLError:
                meta = {}
            return meta, body
    return {}, raw_text


# ---------------------------------------------------------------------------
# Gambar (multimodal)
# ---------------------------------------------------------------------------

def caption_embedded_image(image_path: Path) -> str:
    """
    Modalitas gambar: gambar (mis. diagram alur, screenshot form) diubah jadi
    deskripsi teks lewat model vision Groq, lalu deskripsi itu di-embed di
    ruang vektor yang sama dengan chunk teks. Pendekatan caption-then-embed
    ini dipilih dibanding embedding visual murni (mis. CLIP) karena jauh
    lebih ringan untuk dideploy dan tetap membuat isi gambar bisa diretrieve
    & disitasi seperti chunk teks biasa.
    """
    ext = image_path.suffix.lstrip(".") or "png"
    b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    data_url = f"data:image/{ext};base64,{b64}"
    instruction = (
        "Deskripsikan isi gambar ini secara faktual dan ringkas dalam Bahasa "
        "Indonesia, khusus untuk keperluan pencarian dokumen internal "
        "perusahaan (SOP/kebijakan). Jangan menambahkan opini atau informasi "
        "yang tidak terlihat di gambar."
    )
    return llm.caption_image(data_url, instruction)


# ---------------------------------------------------------------------------
# Pemecahan section & chunk
# ---------------------------------------------------------------------------

def _split_sections(body_text: str) -> list[tuple[str, str]]:
    """Pecah dokumen jadi (judul_section, isi) berbasis heading markdown (#, ##, ###)."""
    lines = body_text.splitlines()
    sections: list[tuple[str, str]] = []
    current_title = "Pendahuluan"
    current_body: list[str] = []

    for line in lines:
        heading_match = re.match(r"^(#{1,3})\s+(.*)", line.strip())
        if heading_match:
            if current_body:
                sections.append((current_title, "\n".join(current_body).strip()))
            current_title = heading_match.group(2).strip()
            current_body = []
        else:
            current_body.append(line)

    if current_body:
        sections.append((current_title, "\n".join(current_body).strip()))

    return [s for s in sections if s[1]]


def _paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def _is_markdown_table(paragraph: str) -> bool:
    lines = [l for l in paragraph.splitlines() if l.strip()]
    return len(lines) >= 2 and lines[0].strip().startswith("|") and lines[1].strip().startswith("|")


def _split_table_by_rows(paragraph: str, size: int) -> list[str]:
    """Pecah tabel markdown per baris data, dengan header+separator diulang
    di setiap chunk supaya tiap baris tetap bisa berdiri sendiri (self-
    contained) saat diretrieve terpisah — tidak pernah memotong satu baris
    tabel di tengah."""
    lines = paragraph.splitlines()
    header, separator = lines[0], lines[1]
    data_rows = lines[2:]

    chunks: list[str] = []
    current_rows: list[str] = []
    for row in data_rows:
        candidate_rows = current_rows + [row]
        candidate_text = "\n".join([header, separator, *candidate_rows])
        if len(candidate_text) <= size or not current_rows:
            current_rows = candidate_rows
        else:
            chunks.append("\n".join([header, separator, *current_rows]))
            current_rows = [row]
    if current_rows:
        chunks.append("\n".join([header, separator, *current_rows]))
    return chunks


def _pack_paragraphs(paragraphs: list[str], size: int, overlap: int) -> list[str]:
    """Kemas paragraf berurutan ke dalam chunk hingga mendekati `size`,
    tanpa pernah memotong sebuah paragraf di tengah kecuali paragraf itu
    sendiri lebih panjang dari `size`. Tabel markdown yang kepanjangan
    dipecah per-baris (lihat _split_table_by_rows), bukan per-karakter,
    supaya satu baris tabel (mis. satu baris matriks prioritas) tidak
    pernah terpotong di tengah kolom."""
    chunks: list[str] = []
    current = ""

    for para in paragraphs:
        candidate = f"{current}\n\n{para}" if current else para
        if len(candidate) <= size:
            current = candidate
            continue

        if current:
            chunks.append(current)

        if len(para) <= size:
            current = para
        elif _is_markdown_table(para):
            chunks.extend(_split_table_by_rows(para, size))
            current = ""
        else:
            start = 0
            while start < len(para):
                end = start + size
                chunks.append(para[start:end])
                start = end - overlap
            current = ""

    if current:
        chunks.append(current)
    return chunks


def _split_faq_qa(body: str) -> list[str]:
    """Pecah blok FAQ per pasangan tanya-jawab (setiap blok diawali '**T:')."""
    parts = re.split(r"(?=\*\*T:)", body)
    return [p.strip() for p in parts if p.strip()]


def _looks_like_faq(section_title: str, body: str) -> bool:
    return section_title.strip().lower().startswith("pertanyaan") or body.count("**T:") >= 2


def classify_section_version(
    section_title: str,
    section_body: str,
    default_version: str,
    default_is_active: bool,
) -> tuple[str, bool]:
    """Hanya menandai NONAKTIF bila judul section eksplisit memuat kata
    'NONAKTIF' (konvensi dokumen ini), atau body memuat metadata inline
    eksplisit `is_active: false`. Kata 'v1.4' yang muncul di narasi lain
    (riwayat perubahan, penjelasan pengganti) TIDAK memicu status nonaktif —
    itu bukan isi arsip, hanya referensi ke versi lama."""
    if _NONAKTIF_IN_TITLE.search(section_title) or _INLINE_INACTIVE_META.search(section_body):
        version_match = _VERSION_IN_TITLE.search(section_title)
        old_version = version_match.group(1) if version_match else "arsip"
        return old_version, False
    return default_version, default_is_active


def build_chunks_from_document(path: Path) -> tuple[dict[str, Any], list[SourceChunk]]:
    raw_text = load_raw_text(path)
    doc_meta, body_text = _extract_frontmatter(raw_text)

    default_version = str(doc_meta.get("doc_version", _ACTIVE_VERSION_LABEL_FALLBACK))
    default_is_active = bool(doc_meta.get("is_active", True))

    sections = _split_sections(body_text)

    chunks: list[SourceChunk] = []
    for section_title, body in sections:
        doc_version, is_active = classify_section_version(
            section_title, body, default_version, default_is_active
        )

        if _looks_like_faq(section_title, body):
            pieces = _split_faq_qa(body)
        else:
            pieces = _pack_paragraphs(_paragraphs(body), CHUNK_SIZE, CHUNK_OVERLAP)

        for piece in pieces:
            chunks.append(
                SourceChunk(
                    chunk_id=str(uuid.uuid4()),
                    text=piece,
                    section_title=section_title,
                    doc_version=doc_version,
                    is_active=is_active,
                )
            )

    return doc_meta, chunks


def build_chunks_from_image(path: Path, section_title: str = "Lampiran Gambar") -> list[SourceChunk]:
    caption = caption_embedded_image(path)
    return [
        SourceChunk(
            chunk_id=str(uuid.uuid4()),
            text=caption,
            section_title=section_title,
            doc_version=_ACTIVE_VERSION_LABEL_FALLBACK,
            is_active=True,
            modality="image",
            extra={"source_image": str(path)},
        )
    ]
