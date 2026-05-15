FROM python:3.11-slim

# 1. Install uv as root
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 2. Set up the non-root user shell profile but STAY as root for now
RUN useradd -m -u 1000 user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# 3. Copy lockfiles and install dependencies system-wide
COPY pyproject.toml uv.lock ./
RUN uv pip install --system --no-cache -r pyproject.toml

# 4. NOW switch to the non-root user for security compliance
USER user

# 5. Copy your application source code and grant ownership to the user
COPY --chown=user:user . .

# FORCE Python to look inside the current app directory for modules like main, routes, etc.
ENV PYTHONPATH=$HOME/app

EXPOSE 7860

# Running Uvicorn directly by pointing explicitly to the file path
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "7860", "--workers", "1"]