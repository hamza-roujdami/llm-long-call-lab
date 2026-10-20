FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /srv
RUN pip install --no-cache-dir "fastapi>=0.115" "uvicorn>=0.32" "pydantic-settings>=2.6"
COPY mock/ ./mock/
RUN useradd --system --uid 10001 app
USER app
EXPOSE 8000
# Long keep-alive so uvicorn never closes an idle connection before the timeouts under test.
CMD ["uvicorn", "mock.app:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "3600"]
