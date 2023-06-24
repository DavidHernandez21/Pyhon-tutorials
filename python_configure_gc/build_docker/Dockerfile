FROM python:3.11.0-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    TEST_USER=test \
    TEST_GROUP=test

RUN pip install --no-cache-dir psutil colorama && \
    groupadd -g 1000 ${TEST_GROUP} && \
    useradd -rm -d /home/${TEST_USER} -s /bin/bash -g ${TEST_GROUP} -u 1000 ${TEST_USER}

USER ${TEST_USER}
