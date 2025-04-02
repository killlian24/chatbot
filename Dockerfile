FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir fastapi uvicorn langchain chromadb requests

CMD ["uvicorn", "chat_server:app", "--host", "0.0.0.0", "--port", "8000"]
