FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /srv
RUN pip install --no-cache-dir "openai>=1.109" "httpx>=0.28" "pydantic-settings>=2.6" \
    "azure-identity>=1.19" "aiohttp>=3.10"
COPY worker/ ./worker/
COPY data/synthetic_docs/facts.jsonl ./data/synthetic_docs/facts.jsonl
RUN useradd --system --uid 10001 app
USER app
ENTRYPOINT ["python", "-m", "worker"]
