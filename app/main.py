from __future__ import annotations

import logging
import uuid

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.schemas import AskRequest, AskResponse, HealthResponse
from app.security import secure_hash_log
from app.services import agent, database, embedder

settings = get_settings()

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger("nusantaracare_rag")

app = FastAPI(
    title="NusantaraCare RAG API",
    version="1.0.0",
    description=(
        "Asisten GenAI berbasis RAG untuk dokumen operasional internal "
        "NusantaraCare. Jawaban hanya berdasarkan dokumen, menyertakan "
        "sitasi sumber, dan dapat dibedakan antara ketentuan aktif (v2.0) "
        "dan arsip nonaktif (v1.4)."
    ),
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "message": "NusantaraCare RAG API aktif. Kunjungi /docs untuk Swagger UI.",
        "health": "/health",
        "ask": "/ask (POST)",
    }


@app.get("/health", response_model=HealthResponse)
def health_check():
    """
    Health check JUJUR (bukan {"status": "ok"} tanpa verifikasi) — memeriksa
    komponen nyata: index vektor terisi, dan model embedding bisa dipanggil.
    LLM Groq TIDAK dipanggil di sini supaya health check tetap murah/cepat
    dan tidak membebani rate limit.
    """
    components: dict[str, str] = {}

    try:
        chunk_count = database.count()
        components["vector_db"] = "ok" if chunk_count > 0 else "empty_index"
    except Exception as exc:  # noqa: BLE001
        components["vector_db"] = f"failed: {exc}"

    try:
        embedder.embed_query("healthcheck")
        components["embedding_model"] = "ok"
    except Exception as exc:  # noqa: BLE001
        components["embedding_model"] = f"failed: {exc}"

    components["llm_api_key_configured"] = "ok" if settings.groq_api_key else "missing"

    # "empty_index" dilaporkan apa adanya (jujur ke pemanggil) tapi tidak
    # dianggap degraded — itu kondisi normal pada instalasi baru sebelum
    # build_index.py dijalankan. Hanya kegagalan nyata yang menurunkan status.
    global_status = "ok"
    if components["vector_db"].startswith("failed"):
        global_status = "degraded"
    if components["embedding_model"] != "ok":
        global_status = "degraded"
    if components["llm_api_key_configured"] != "ok":
        global_status = "degraded"

    return HealthResponse(status=global_status, version="1.0.0", components=components)


@app.post("/ask", response_model=AskResponse)
def ask_endpoint(request: AskRequest):
    trace_id = f"trace_{uuid.uuid4().hex[:10]}"
    hashed_q = secure_hash_log(request.question)
    logger.info("Request diterima | mode=%s | question_hash=%s", request.mode, hashed_q)

    try:
        return agent.handle_ask(
            question=request.question,
            mode=request.mode,
            image_base64=request.image_base64,
            trace_id=trace_id,
        )
    except RuntimeError as exc:
        # mis. GROQ_API_KEY belum di-set
        logger.error("[trace=%s] Config error: %s", trace_id, exc)
        raise HTTPException(status_code=503, detail={"reason_code": "service_misconfigured", "message": str(exc)})
    except Exception as exc:  # noqa: BLE001
        logger.error("[trace=%s] Kegagalan internal: %s", trace_id, exc)
        raise HTTPException(
            status_code=500,
            detail={"reason_code": "internal_error", "message": "Terjadi kendala internal pada server."},
        )
