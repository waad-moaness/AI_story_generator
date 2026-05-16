FROM python:3.11-slim

# 1. Install uv as root for ultra-fast package installation
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 2. Set up the non-root user but stay as root for dependency installation
RUN useradd -m -u 1000 user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# We use a distinct workspace directory to avoid any folder name confusion
WORKDIR $HOME/workspace

# 3. Copy lockfiles and install dependencies system-wide
COPY pyproject.toml uv.lock ./
RUN uv pip install --system --no-cache -r pyproject.toml

# 4. Copy your entire local project (including your 'app' folder) into the workspace
COPY --chown=user:user . .

# 5. Switch to the secure non-root user for Hugging Face compliance
USER user

# Tell Python to use the workspace root so your 'from app.models import ...' statements resolve perfectly
ENV PYTHONPATH=$HOME/workspace

EXPOSE 7860

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860", "--workers", "1"]