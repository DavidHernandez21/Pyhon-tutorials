FROM python:3.11.4-slim
RUN apt update && apt install -y gdb procps && \
    apt clean -y && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -U debugpy

ENV DEBUGPY_LOG_DIR=/logs
