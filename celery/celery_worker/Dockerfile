FROM python:3.10.5-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# layer caching for faster builds
COPY ./requirements.txt requirements.txt
RUN  apt update -y && apt upgrade -y && apt autoremove -y && pip install --no-cache-dir -U pip && pip install --no-cache-dir -r requirements.txt

#COPY app.py /app.py
COPY ./tasks.py /celery_worker/tasks.py
WORKDIR /celery_worker

RUN addgroup --gid 1001 --system app && \
    adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

USER app
