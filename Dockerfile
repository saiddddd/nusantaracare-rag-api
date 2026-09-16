# Dasar image Python minimalis
FROM python:3.11-slim

WORKDIR /app

# Copy requirements dulu untuk caching layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh kode + data dokumen (WAJIB ikut sesuai brief final project)
COPY app ./app
COPY data ./data

EXPOSE 8000

# Index dibangun saat image start (bukan saat build) supaya selalu memakai
# GROQ_API_KEY runtime yang benar (dibutuhkan untuk captioning gambar bila
# ada). Untuk dokumen tanpa gambar, langkah ini cepat karena hanya embedding
# lokal.
CMD sh -c "python -m app.scripts.build_index && uvicorn app.main:app --host 0.0.0.0 --port 8000"
