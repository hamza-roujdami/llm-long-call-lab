FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /srv
RUN pip install --no-cache-dir "fastapi>=0.115" "uvicorn>=0.32" "httpx>=0.28" \
    "azure-identity>=1.19" "aiohttp>=3.10"
COPY api/ ./api/
RUN useradd --system --uid 10001 app
USER app
EXPOSE 8080
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8080"]
