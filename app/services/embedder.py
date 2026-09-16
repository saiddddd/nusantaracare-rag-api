"""
Embedding lokal via FastEmbed (ONNX Runtime) — BUKAN sentence-transformers +
torch.

Alasan pergantian: kombinasi torch + sentence-transformers ternyata terlalu
berat untuk RAM instance gratis di FastAPI Cloud (deployment sempat gagal
dengan status "Verification Failed (OOM)"). FastEmbed menjalankan model
embedding lewat ONNX Runtime murni (model terkuantisasi, ~220MB), tanpa
perlu memuat seluruh framework PyTorch ke memori — jauh lebih ringan untuk
container kecil, dengan kualitas embedding yang setara untuk model ini.

Model: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 —
mendukung ~50 bahasa termasuk Indonesia. Model ini simetris (bukan gaya E5),
sehingga query dan dokumen TIDAK butuh prefix khusus yang berbeda — dua
fungsi di bawah (embed_texts untuk dokumen, embed_query untuk pertanyaan)
tetap dipisah demi konsistensi API bila suatu saat model diganti ke
keluarga E5 yang memang membutuhkan prefix "query: "/"passage: " berbeda.
"""
from __future__ import annotations

from functools import lru_cache

from fastembed import TextEmbedding

from app.config import get_settings

_settings = get_settings()


@lru_cache
def _get_model() -> TextEmbedding:
    return TextEmbedding(model_name=_settings.embedding_model_name)


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Untuk dokumen/chunk yang akan disimpan ke index (bukan query)."""
    if not texts:
        return []
    model = _get_model()
    return [vector.tolist() for vector in model.embed(texts)]


def embed_query(text: str) -> list[float]:
    """Untuk pertanyaan pengguna saat retrieval."""
    model = _get_model()
    vectors = list(model.query_embed([text]))
    return vectors[0].tolist()