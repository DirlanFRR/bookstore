# `python-base` sets up all our shared environment variables
FROM python:3.12-slim as python-base

# Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=2.0.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Add Poetry and virtual environment to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install system dependencies in a single step
RUN apt-get update && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        git \
        libpq-dev \
        gcc \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip \
    && pip install "poetry==2.0.1"

# Set up project directory
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml README.md ./ 

# Install dependencies without dev dependencies and without installing the project itself
RUN poetry install --without dev --no-cache --no-root

# Ensure Git is configured for GitPython
ENV GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git

# Set working directory for application
WORKDIR /app
COPY . /app/

EXPOSE 8000

CMD ["bash", "-c", "python manage.py runserver 0.0.0.0:8000"]
