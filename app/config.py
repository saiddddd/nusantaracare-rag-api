"""
Konfigurasi terpusat aplikasi.

Semua nilai sensitif (API key) WAJIB datang dari environment variable / .env,
tidak pernah di-hardcode di kode. Lihat .env.example untuk daftar variabel
yang dibutuhkan.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # --- Groq LLM ---
    groq_api_key: str = ""
    groq_text_model: str = "openai/gpt-oss-120b"
    groq_vision_model: str = "qwen/qwen3.6-27b"

    # --- Embeddings ---
    embedding_model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

    # --- Vector DB ---
    chroma_persist_dir: str = "data/index"
    chroma_collection_name: str = "nusantaracare_kb"

    # --- Retrieval ---
    retrieval_top_k: int = 5
    retrieval_min_similarity: float = 0.35

    # --- App ---
    app_env: str = "local"
    log_level: str = "INFO"

    @property
    def project_root(self) -> Path:
        return Path(__file__).resolve().parent.parent

    @property
    def raw_docs_dir(self) -> Path:
        return self.project_root / "data" / "raw_docs"

    @property
    def chroma_persist_path(self) -> Path:
        p = self.project_root / self.chroma_persist_dir
        p.mkdir(parents=True, exist_ok=True)
        return p


@lru_cache
def get_settings() -> Settings:
    return Settings()
