FROM python:3.11.4-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade debugpy -r /code/requirements.txt
# RUN pip install debugpy

COPY ./main.py ./__init__.py /code/app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
