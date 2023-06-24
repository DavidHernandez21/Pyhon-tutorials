FROM pypy:3.9-bullseye AS builder

ENV VENV_NAME=venv

RUN apt update -y && \
    apt upgrade -y && \
    apt autoremove -y && \
    pip3 install -U --no-cache-dir pip virtualenv &&\
    virtualenv ${VENV_NAME} && \
    . ${VENV_NAME}/bin/activate && \
    pip3 install -U --no-cache-dir pip numpy


FROM pypy:3.9-slim

WORKDIR /app

ENV VENV_NAME=venv

COPY --from=builder /${VENV_NAME} /${VENV_NAME}

RUN apt update -y && \
    apt upgrade -y && \
    apt autoremove -y
