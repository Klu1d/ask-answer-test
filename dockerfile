FROM python:3.12-slim

RUN pip install uv

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

RUN uv venv /app/.venv

COPY . /app

RUN uv pip install .

RUN chmod +x start.sh

EXPOSE 8000

CMD ["./start.sh"]
