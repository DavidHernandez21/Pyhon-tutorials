FROM python:3-slim

ENV PYTHONUNBUFFERED=1

# layer caching for faster builds
COPY ./requirements.txt requirements.txt
RUN apt update -y && \
    apt upgrade -y && \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists && \
    pip install --no-cache-dir -U pip && pip install --no-cache-dir -r requirements.txt

#COPY app.py /app.py
COPY ./send_task.py /celery_worker/send_task.py
WORKDIR /celery_worker

RUN addgroup --gid 1001 --system app && \
    adduser --no-create-home --shell /bin/bash --disabled-password --uid 1001 --system --group app

USER app
