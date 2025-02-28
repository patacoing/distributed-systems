FROM python:3.10.15-alpine3.20 AS base_image

FROM base_image AS deps

WORKDIR /app

RUN apk add curl && curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/bin" sh && mkdir -p /deps

COPY pyproject.toml uv.lock .python-version ./

RUN /bin/uv sync --frozen --no-install-project --no-editable


FROM base_image AS final

WORKDIR /app

ENV PYTHONPATH="${PYTHONPATH}:/deps"

COPY --from=deps /app/.venv/lib/python3.10/site-packages /deps

COPY . .

CMD ["python", "-m", "fastapi", "run", "main.py", "--host", "0.0.0.0"]