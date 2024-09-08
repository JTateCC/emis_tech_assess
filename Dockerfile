# 1. Use a lightweight Python image from Docker Hub as the base
FROM python:3.11-slim


WORKDIR /usr/src/app


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
