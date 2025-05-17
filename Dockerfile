# ---------- Stage 1: Build ----------
FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.1.3

# Install Poetry and system deps
RUN apt-get update && apt-get install -y curl build-essential \
  && pip install "poetry==$POETRY_VERSION"

#RUN poetry --version

WORKDIR /app

COPY mvp_be /app/mvp_be
# Copy only dependency declarations
COPY pyproject.toml poetry.lock* README.md /app/

# Install deps (no venv, faster for Docker)
RUN poetry config virtualenvs.create false && poetry install --only main --no-root --no-interaction --no-ansi



# Copy full source
COPY . /app


# ---------- Stage 2: Runtime ----------
FROM python:3.13-slim

#RUN apt-get purge -y build-essential curl && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
# Copy installed packages and source code from builder
COPY --from=builder /app /app

WORKDIR /app

# Expose port (FastAPI default)
EXPOSE 8080

# Optional: use a non-root user for security
RUN adduser --disabled-password appuser && chown -R appuser /app
USER appuser

# Start FastAPI with Uvicorn
CMD ["uvicorn", "mvp_be.main:app", "--host", "0.0.0.0", "--port", "8080"]
