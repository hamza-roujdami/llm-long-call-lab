FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1 RESULTS_DIR=/tmp/results
WORKDIR /srv
RUN pip install --no-cache-dir "httpx>=0.28" "pydantic-settings>=2.6"
COPY probe/__init__.py ./probe/__init__.py
COPY probe/job/ ./probe/job/
RUN useradd --system --uid 10001 app
USER app
# Scenario is chosen at job start (SCENARIO env var or --args "--scenario <name>").
ENTRYPOINT ["python", "-m", "probe.job.run"]
