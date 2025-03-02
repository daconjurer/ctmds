# syntax = docker/dockerfile:1.2

# Build argument for Python version
ARG PYTHON_VERSION=3.12

# Platform args for multi-arch builds
ARG TARGETARCH
ARG TARGETPLATFORM=linux/amd64

FROM --platform=$TARGETPLATFORM python:${PYTHON_VERSION}-slim as python-base

# Builder stage
FROM python-base as builder

ARG POETRY_VERSION=2.0.1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY ctmds ./ctmds
RUN pip install poetry==${POETRY_VERSION} && \
    touch README.md && \
    poetry config virtualenvs.in-project true && \
    poetry install --without dev

ENV PATH="/app/.venv/bin:$PATH"

# Development stage
FROM builder as dev

CMD ["python3", "-m", "ctmds.main"]

# Production stage
FROM builder as api

VOLUME /app/data

COPY .env ./
CMD ["python3", "-m", "ctmds.main"]
