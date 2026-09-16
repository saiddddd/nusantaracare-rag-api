"""
Lapisan "agentic" tipis di atas RAG murni.

Kenapa dipisah dari rag.py? Supaya /ask?mode=rag bisa dites secara terisolasi
(langsung retrieve+jawab tanpa router), sedangkan /ask?mode=agentic melewati
pemeriksaan keamanan & routing intent dulu. Ini memudahkan debugging sesuai
saran materi OpenClaw: "pisahkan lapisan supaya kalau ada yang gagal, jelas
sumbernya dari mana".

Alur agentic:
  1. Screening prompt-injection (security.py) -> kalau lolos aturan
     mencurigakan, blokir SEBELUM menyentuh LLM sama sekali.
  2. Deteksi off-topic super ringan (sapaan/basa-basi) -> jawab singkat tanpa
     memboroskan panggilan LLM/retrieval.
  3. Selain itu -> serahkan ke pipeline RAG (rag.py), yang punya logika
     grounding, confidence, dan penanganan versi dokumen sendiri.
"""
from __future__ import annotations

import re

from app.schemas import AskResponse, Citation
from app.security import looks_like_prompt_injection
from app.services import rag

_GREETING_PATTERN = re.compile(
    r"^\s*(hai|halo|hello|hi|pagi|siang|sore|malam|terima\s*kasih|thanks|makasih)\b[\s!.,]*$",
    re.I,
)


def _blocked_response(trace_id: str, mode: str) -> AskResponse:
    return AskResponse(
        answer=(
            "Permintaan Anda terdeteksi mengandung pola instruksi yang tidak "
            "sesuai kebijakan asisten ini (mis. mencoba mengubah aturan sistem). "
            "Silakan ajukan pertanyaan seputar dokumen operasional NusantaraCare."
        ),
        citations=[],
        trace_id=trace_id,
        mode=mode,
        confidence_label="low",
        reason_code="prompt_injection_blocked",
    )


def _greeting_response(trace_id: str, mode: str) -> AskResponse:
    return AskResponse(
        answer=(
            "Halo! Saya asisten dokumen internal NusantaraCare. Silakan tanyakan "
            "sesuatu seputar SOP, kebijakan, atau FAQ yang ada di panduan "
            "operasional internal."
        ),
        citations=[],
        trace_id=trace_id,
        mode=mode,
        confidence_label="high",
        reason_code="off_topic",
    )


def handle_ask(question: str, mode: str, image_base64: str | None, trace_id: str) -> AskResponse:
    if looks_like_prompt_injection(question):
        return _blocked_response(trace_id, mode)

    if image_base64:
        # Query multimodal — deteksi tipe gambar sederhana dari header base64
        # kalau tidak ada prefix data URL, asumsikan PNG.
        image_data_url = (
            image_base64 if image_base64.startswith("data:") else f"data:image/png;base64,{image_base64}"
        )
        result = rag.answer_multimodal_question(question, image_data_url)
        return AskResponse(
            answer=result.answer,
            citations=result.citations,
            trace_id=trace_id,
            mode=mode,
            confidence_label=result.confidence_label,
            reason_code=result.reason_code,
        )

    if mode == "agentic" and _GREETING_PATTERN.match(question):
        return _greeting_response(trace_id, mode)

    result = rag.answer_question(question)
    return AskResponse(
        answer=result.answer,
        citations=result.citations,
        trace_id=trace_id,
        mode=mode,
        confidence_label=result.confidence_label,
        reason_code=result.reason_code,
    )
