"""
Wrapper di atas ChromaDB (PersistentClient) — dipilih karena:
  - Metadata filtering built-in (kita pakai untuk membedakan chunk
    doc_version="2.0" is_active=True vs arsip v1.4 is_active=False).
  - Persist ke disk lokal (folder data/index/), tidak butuh server terpisah,
    cocok untuk deployment single-container di FastAPI Cloud.
  - API Python yang sederhana untuk skala dokumen kelas ini (satu panduan
    operasional, bukan jutaan dokumen — FAISS lebih relevan untuk skala jauh
    lebih besar dan butuh index tuning manual, overkill di sini).
"""
from __future__ import annotations

from functools import lru_cache
from typing import Any

import chromadb
from chromadb.config import Settings as ChromaSettings

from app.config import get_settings

_settings = get_settings()


@lru_cache
def _get_client() -> chromadb.ClientAPI:
    return chromadb.PersistentClient(
        path=str(_settings.chroma_persist_path),
        settings=ChromaSettings(anonymized_telemetry=False),
    )


@lru_cache
def _get_collection():
    client = _get_client()
    return client.get_or_create_collection(
        name=_settings.chroma_collection_name,
        metadata={"hnsw:space": "cosine"},
    )


def reset_collection() -> None:
    """Dipakai oleh scripts/build_index.py sebelum re-index penuh."""
    client = _get_client()
    try:
        client.delete_collection(_settings.chroma_collection_name)
    except Exception:
        pass
    _get_collection.cache_clear()
    _get_collection()


def upsert_chunks(
    ids: list[str],
    embeddings: list[list[float]],
    documents: list[str],
    metadatas: list[dict[str, Any]],
) -> None:
    collection = _get_collection()
    collection.upsert(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)


def count() -> int:
    return _get_collection().count()


def query(
    embedding: list[float],
    top_k: int,
    where: dict[str, Any] | None = None,
) -> dict[str, Any]:
    collection = _get_collection()
    return collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        where=where,
        include=["documents", "metadatas", "distances"],
    )
