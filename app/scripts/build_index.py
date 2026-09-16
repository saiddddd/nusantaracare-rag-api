"""
Jalankan sekali (dan setiap kali dokumen sumber berubah):

    python -m app.scripts.build_index

Script ini TIDAK mengubah file di data/raw_docs/ — ia hanya membacanya,
lalu menulis embedding + metadata ke data/index/ (ChromaDB persistent store,
di-gitignore karena bisa dibangun ulang kapan saja dari sumbernya).
"""
from __future__ import annotations

import sys
from pathlib import Path

from app.config import get_settings
from app.services import database, embedder, ingestion

SUPPORTED_DOC_EXT = {".md", ".markdown", ".txt", ".pdf", ".docx"}
SUPPORTED_IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}


def main() -> None:
    settings = get_settings()
    raw_dir = settings.raw_docs_dir
    if not raw_dir.exists():
        print(f"[ERROR] Folder tidak ditemukan: {raw_dir}", file=sys.stderr)
        sys.exit(1)

    files = sorted(p for p in raw_dir.iterdir() if p.is_file())
    if not files:
        print(f"[ERROR] Tidak ada dokumen di {raw_dir}. Taruh file sumber di sana dulu.")
        sys.exit(1)

    print("[1/4] Mengosongkan index lama...")
    database.reset_collection()

    all_ids, all_embeds, all_docs, all_meta = [], [], [], []

    for file_path in files:
        suffix = file_path.suffix.lower()
        # default fallback bila dokumen tidak punya frontmatter metadata
        doc_id = file_path.stem
        doc_title = file_path.stem.replace("_", " ").title()

        if suffix in SUPPORTED_DOC_EXT:
            print(f"[2/4] Memproses dokumen teks: {file_path.name}")
            doc_meta, chunks = ingestion.build_chunks_from_document(file_path)
            doc_id = str(doc_meta.get("doc_id", doc_id))
            doc_title = str(doc_meta.get("doc_title", doc_title))
        elif suffix in SUPPORTED_IMAGE_EXT:
            print(f"[2/4] Memproses gambar (captioning via Groq vision): {file_path.name}")
            chunks = ingestion.build_chunks_from_image(file_path)
        else:
            print(f"    - lewati (format tidak didukung): {file_path.name}")
            continue

        print(f"    -> {len(chunks)} chunk dihasilkan")
        texts = [c.text for c in chunks]
        vectors = embedder.embed_texts(texts)

        for chunk, vector in zip(chunks, vectors):
            all_ids.append(chunk.chunk_id)
            all_embeds.append(vector)
            all_docs.append(chunk.text)
            all_meta.append(
                {
                    "doc_id": doc_id,
                    "doc_title": doc_title,
                    "chunk_id": chunk.chunk_id,
                    "section_title": chunk.section_title,
                    "doc_version": chunk.doc_version,
                    "is_active": chunk.is_active,
                    "modality": chunk.modality,
                }
            )

    print(f"[3/4] Menyimpan {len(all_ids)} chunk ke ChromaDB ({settings.chroma_persist_path})...")
    database.upsert_chunks(all_ids, all_embeds, all_docs, all_meta)

    print(f"[4/4] Selesai. Total chunk ter-index: {database.count()}")


if __name__ == "__main__":
    main()
