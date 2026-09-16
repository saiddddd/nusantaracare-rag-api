"""
Kontrak skema data (Pydantic v2). Ini adalah "janji tertulis" format API —
lihat materi Sesi FastAPI: skema tidak boleh berubah sewaktu-waktu tanpa
versi baru.
"""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# /ask
# ---------------------------------------------------------------------------

class AskRequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=1000, description="Pertanyaan pengguna")
    mode: Literal["rag", "agentic"] = Field(
        default="agentic",
        description="'rag' = selalu retrieve+jawab; 'agentic' = router memutuskan alur",
    )
    # Multimodal: pengguna boleh melampirkan satu gambar (mis. screenshot form,
    # foto dokumen fisik) untuk ditanyakan bersamaan dengan teks.
    image_base64: Optional[str] = Field(
        default=None,
        description="Gambar terenkode base64 (opsional) untuk pertanyaan multimodal",
    )


class Citation(BaseModel):
    doc_id: str
    chunk_id: str
    doc_title: str
    section_title: str
    doc_version: str
    is_active: bool
    modality: Literal["text", "image"] = "text"


class AskResponse(BaseModel):
    answer: str
    citations: list[Citation]
    trace_id: str
    mode: Literal["rag", "agentic"]
    confidence_label: Literal["high", "medium", "low"]
    reason_code: Literal[
        "answered",
        "no_relevant_context",
        "conflicting_sources",
        "off_topic",
        "prompt_injection_blocked",
    ]


# ---------------------------------------------------------------------------
# /health
# ---------------------------------------------------------------------------

class HealthResponse(BaseModel):
    status: Literal["ok", "degraded"]
    version: str
    components: dict[str, str]
