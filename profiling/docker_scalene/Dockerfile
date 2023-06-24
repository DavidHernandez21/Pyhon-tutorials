FROM python:3.10.5-slim

RUN pip install -U pip scalene numpy memray yelp-gprof2dot snakeviz httpx requests && apt update -y && apt upgrade -y && apt autoremove -y && apt install graphviz -y

WORKDIR /app
