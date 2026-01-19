# Tells Docker which language version of Dockerfiles we're using
# safe to ignore, safe to include
# syntax=docker/dockerfile:1.7

FROM python:3.12-slim AS base

# stop python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Force python to print logs immediately
ENV PYTHONUNBUFFERED=1
# Use .venv/ as project's VM
ENV UV_PROJECT_ENVIRONMENT=.venv
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Install curl for uv installer
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Copy only dependency files first (better cache)
COPY pyproject.toml uv.lock ./

# Sync dependencies from lockfile (reproducible)
RUN uv sync --frozen --no-dev

# Copy your app code (and anything else you need at runtime)
COPY app ./app

# Just documenting that app listens to port 8000 not that it opens port
EXPOSE 8000

# Run via uv to guarantee correct environment
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
