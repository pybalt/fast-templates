FROM python:latest

WORKDIR /app

ADD . /app/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir -r requirements.txt