"""
Wrapper tipis di atas Groq SDK.

Dua model dipakai untuk dua tujuan berbeda (jangan dicampur):
- groq_text_model   : sintesis jawaban berbasis konteks teks yang di-retrieve.
- groq_vision_model : (a) captioning gambar saat ingestion (dokumen bergambar),
                       (b) menjawab pertanyaan yang melampirkan gambar (query
                       multimodal).

Retry HANYA untuk error yang sifatnya sementara (rate limit 429, atau error
server Groq 5xx) — bukan untuk 400 Bad Request, yang berarti request kita
sendiri yang salah bentuk dan tidak akan pernah berhasil walau diulang.
Mengulang error 400 hanya membuang kuota dan bisa memicu rate limit
tambahan (429) dari pengulangan itu sendiri.

`reraise=True` memastikan setelah retry habis, exception ASLI dari Groq
(lengkap dengan status code & body) yang naik ke pemanggil — bukan
`tenacity.RetryError` generik yang menyembunyikan detail penyebabnya.
"""
from __future__ import annotations

import logging

from groq import APIStatusError, Groq
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from app.config import get_settings

logger = logging.getLogger("nusantaracare_rag.llm")

_settings = get_settings()
_client: Groq | None = None

_RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


def _get_client() -> Groq:
    global _client
    if _client is None:
        if not _settings.groq_api_key:
            raise RuntimeError(
                "GROQ_API_KEY belum di-set. Isi file .env (lihat .env.example)."
            )
        _client = Groq(api_key=_settings.groq_api_key)
    return _client


def _is_transient(exc: BaseException) -> bool:
    status = getattr(exc, "status_code", None)
    # Error tanpa status_code (mis. gangguan jaringan) tetap dianggap layak
    # dicoba ulang; error dengan status code di luar daftar transient
    # (mis. 400, 401, 404) TIDAK diulang.
    return status is None or status in _RETRYABLE_STATUS_CODES


def _log_groq_error(context: str, exc: Exception) -> None:
    status = getattr(exc, "status_code", "?")
    body = getattr(exc, "body", None) or getattr(exc, "message", None) or str(exc)
    logger.error("Groq API error saat %s | status=%s | detail=%s", context, status, body)


_retry_transient = retry(
    wait=wait_exponential(multiplier=1, min=1, max=10),
    stop=stop_after_attempt(3),
    retry=retry_if_exception(_is_transient),
    reraise=True,
)


@_retry_transient
def generate_answer(system_prompt: str, user_prompt: str, *, temperature: float = 0.1) -> str:
    """Panggilan teks murni untuk sintesis jawaban RAG."""
    client = _get_client()
    try:
        completion = client.chat.completions.create(
            model=_settings.groq_text_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_completion_tokens=800,
        )
    except APIStatusError as exc:
        _log_groq_error("generate_answer", exc)
        raise
    return completion.choices[0].message.content or ""


@_retry_transient
def caption_image(image_data_url: str, instruction: str) -> str:
    """
    Panggilan vision. `image_data_url` harus dalam format
    "data:image/<ext>;base64,<...>" (lihat services/ingestion.py / api util).
    """
    client = _get_client()
    try:
        completion = client.chat.completions.create(
            model=_settings.groq_vision_model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": instruction},
                        {"type": "image_url", "image_url": {"url": image_data_url}},
                    ],
                }
            ],
            temperature=0.2,
            max_completion_tokens=500,
        )
    except APIStatusError as exc:
        _log_groq_error("caption_image", exc)
        raise
    return completion.choices[0].message.content or ""


@_retry_transient
def answer_with_image(system_prompt: str, question: str, context_text: str, image_data_url: str) -> str:
    """
    Query multimodal: pengguna melampirkan gambar + pertanyaan. Konteks teks
    hasil retrieval (jika ada) tetap disertakan supaya jawaban tetap grounded
    ke dokumen, bukan cuma deskripsi gambar bebas.
    """
    client = _get_client()
    user_content = [
        {
            "type": "text",
            "text": (
                f"Konteks dokumen (gunakan jika relevan):\n<<<KONTEKS>>>\n{context_text}\n<<<END KONTEKS>>>\n\n"
                f"Pertanyaan pengguna: {question}"
            ),
        },
        {"type": "image_url", "image_url": {"url": image_data_url}},
    ]
    try:
        completion = client.chat.completions.create(
            model=_settings.groq_vision_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            temperature=0.1,
            max_completion_tokens=800,
        )
    except APIStatusError as exc:
        _log_groq_error("answer_with_image", exc)
        raise
    return completion.choices[0].message.content or ""