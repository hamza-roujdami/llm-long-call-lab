FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /srv
RUN pip install --no-cache-dir "httpx>=0.28" "pydantic-settings>=2.6" "openai>=1.50"
COPY client/ ./client/
RUN useradd --system --uid 10001 app
USER app
# Scenario is chosen at job start (SCENARIO env var or --args "--scenario <name>").
ENTRYPOINT ["python", "-m", "client.run"]
