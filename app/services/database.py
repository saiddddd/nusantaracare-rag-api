"""
Vector store buatan sendiri, berbasis numpy + JSON — BUKAN ChromaDB.

Alasan pergantian: ChromaDB, walau APInya nyaman, membawa banyak dependency
transitif (analytics/telemetry, engine embedded, dll) yang totalnya cukup
berat untuk RAM instance gratis di FastAPI Cloud — dikombinasikan dengan
FastEmbed, deployment tetap kena "Resource limit exceeded" (OOM).

Untuk skala data kelas ini (SATU dokumen, 85 chunk, vektor 384 dimensi —
total cuma sekitar 130KB data vektor), ChromaDB/FAISS sebenarnya overkill.
Brute-force cosine similarity pakai numpy jauh lebih murah secara memori,
tanpa mengorbankan kecepatan (pencarian di antara puluhan/ratusan vektor
levelnya sub-milidetik).

Kontrak fungsi (reset_collection, upsert_chunks, count, query) SENGAJA
dibuat identik dengan versi ChromaDB sebelumnya, termasuk bentuk hasil
query() dan semantik "distance" (1 - cosine_similarity) — supaya
app/services/rag.py tidak perlu diubah sama sekali saat migrasi ini.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from app.config import get_settings

_settings = get_settings()

_STORE: dict[str, Any] | None = None


def _store_path() -> Path:
    return _settings.chroma_persist_path / "store.json"


def _empty_store() -> dict[str, Any]:
    return {"ids": [], "documents": [], "metadatas": [], "embeddings": []}


def _load_store() -> dict[str, Any]:
    global _STORE
    if _STORE is not None:
        return _STORE

    path = _store_path()
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            _STORE = json.load(f)
    else:
        _STORE = _empty_store()
    return _STORE


def _save_store(store: dict[str, Any]) -> None:
    path = _store_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(store, f)


def reset_collection() -> None:
    """Dipakai oleh scripts/build_index.py sebelum re-index penuh."""
    global _STORE
    _STORE = _empty_store()
    _save_store(_STORE)


def upsert_chunks(
    ids: list[str],
    embeddings: list[list[float]],
    documents: list[str],
    metadatas: list[dict[str, Any]],
) -> None:
    store = _load_store()
    existing_index = {chunk_id: i for i, chunk_id in enumerate(store["ids"])}

    for chunk_id, embedding, document, metadata in zip(ids, embeddings, documents, metadatas):
        if chunk_id in existing_index:
            i = existing_index[chunk_id]
            store["embeddings"][i] = embedding
            store["documents"][i] = document
            store["metadatas"][i] = metadata
        else:
            store["ids"].append(chunk_id)
            store["embeddings"].append(embedding)
            store["documents"].append(document)
            store["metadatas"].append(metadata)

    _save_store(store)


def count() -> int:
    return len(_load_store()["ids"])


def _matches_where(metadata: dict[str, Any], where: dict[str, Any] | None) -> bool:
    if not where:
        return True
    return all(metadata.get(key) == value for key, value in where.items())


def query(
    embedding: list[float],
    top_k: int,
    where: dict[str, Any] | None = None,
) -> dict[str, Any]:
    store = _load_store()
    if not store["ids"]:
        return {"ids": [[]], "documents": [[]], "metadatas": [[]], "distances": [[]]}

    candidate_indices = [i for i, meta in enumerate(store["metadatas"]) if _matches_where(meta, where)]
    if not candidate_indices:
        return {"ids": [[]], "documents": [[]], "metadatas": [[]], "distances": [[]]}

    query_vec = np.array(embedding, dtype=np.float32)
    query_norm = np.linalg.norm(query_vec) or 1.0

    scored: list[tuple[float, int]] = []
    for i in candidate_indices:
        vec = np.array(store["embeddings"][i], dtype=np.float32)
        vec_norm = np.linalg.norm(vec) or 1.0
        cosine_similarity = float(np.dot(query_vec, vec) / (query_norm * vec_norm))
        distance = 1.0 - cosine_similarity  # sama seperti konvensi hnsw:space="cosine" ChromaDB
        scored.append((distance, i))

    scored.sort(key=lambda pair: pair[0])
    top = scored[:top_k]

    return {
        "ids": [[store["ids"][i] for _, i in top]],
        "documents": [[store["documents"][i] for _, i in top]],
        "metadatas": [[store["metadatas"][i] for _, i in top]],
        "distances": [[distance for distance, _ in top]],
    }