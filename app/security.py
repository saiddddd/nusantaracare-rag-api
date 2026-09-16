"""
Keamanan aplikasi:

1. Privacy hygiene untuk logging — pertanyaan pengguna TIDAK PERNAH ditulis
   mentah (raw text) ke log server. Kita hanya menulis hash satu arah
   (SHA-256, dipotong 12 karakter) sebagai jejak audit, sesuai materi
   Sesi FastAPI (secure_hash_log).

2. Prompt-injection screening — pertahanan berlapis:
   a) System prompt yang tegas menetapkan hierarki instruksi: HANYA
      instruksi dari developer/system yang dipatuhi. Isi dokumen yang
      diretrieve dan pertanyaan pengguna DIPERLAKUKAN SEBAGAI DATA, bukan
      instruksi, dan dibungkus delimiter eksplisit di dalam prompt (lihat
      services/rag.py).
   b) Heuristic pre-filter di bawah ini menangkap pola injeksi klasik
      (mis. "ignore previous instructions", "abaikan instruksi di atas",
      permintaan membocorkan system prompt / API key) SEBELUM request
      sampai ke LLM. Jika terdeteksi, endpoint langsung menolak dengan
      reason_code="prompt_injection_blocked" tanpa memanggil LLM sama
      sekali (defense-in-depth, bukan cuma mengandalkan model).
"""
from __future__ import annotations

import hashlib
import re

# Pola umum prompt injection (ID + EN). Daftar ini sengaja tidak lengkap
# 100% — ini adalah lapisan pertama, bukan satu-satunya lapisan. Lapisan
# kedua adalah system prompt hardening di rag.py.
_INJECTION_PATTERNS: list[re.Pattern] = [
    re.compile(r"\babaikan\s+(semua\s+)?instruksi\b", re.I),
    re.compile(r"\bignore\s+(all\s+)?(previous|prior|above)\s+instructions?\b", re.I),
    re.compile(r"\bdisregard\s+(the\s+)?(system|previous)\s+prompt\b", re.I),
    re.compile(r"\b(tampilkan|bocorkan|reveal|show)\s+(system\s+prompt|api\s*key|instruksi\s+asli)\b", re.I),
    re.compile(r"\byou\s+are\s+now\b", re.I),
    re.compile(r"\bkamu\s+sekarang\s+(adalah|jadi)\b", re.I),
    re.compile(r"\bact\s+as\s+(if\s+you\s+are\s+)?(dan|developer)\s*mode\b", re.I),
    re.compile(r"\bjailbreak\b", re.I),
    re.compile(r"\bprint\s+your\s+(system|full)\s+prompt\b", re.I),
]


def secure_hash_log(text: str) -> str:
    """Menyamarkan teks sensitif untuk pelaporan log aman (Privacy Hygiene)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def looks_like_prompt_injection(text: str) -> bool:
    """Heuristic cepat, dijalankan sebelum memanggil LLM sama sekali."""
    return any(p.search(text) for p in _INJECTION_PATTERNS)
