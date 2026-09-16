"""
Embedding lokal (bukan lewat Groq — Groq tidak menyediakan endpoint embedding).

Kita pakai sentence-transformers multilingual yang cukup kecil untuk
dideploy (~470MB), tapi tetap punya kualitas retrieval yang layak untuk
Bahasa Indonesia: paraphrase-multilingual-MiniLM-L12-v2.

Model di-load sekali (singleton) dan dipakai baik untuk indexing (ingestion)
maupun query time, supaya representasi vektor konsisten.
"""
from __future__ import annotations

from functools import lru_cache

from sentence_transformers import SentenceTransformer

from app.config import get_settings

_settings = get_settings()


@lru_cache
def _get_model() -> SentenceTransformer:
    return SentenceTransformer(_settings.embedding_model_name)


def embed_texts(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []
    model = _get_model()
    vectors = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
    return vectors.tolist()


def embed_query(text: str) -> list[float]:
    return embed_texts([text])[0]
