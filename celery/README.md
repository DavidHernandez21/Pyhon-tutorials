references [this](https://github.com/veryacademy/YT_FastAPI_Celery_Redis_Flower_Introduction) and [another one](https://github.com/soumilshah1995/Python-Flask-Redis-Celery-Docker)

celery [documentation](https://docs.celeryq.dev/en/stable/index.html)

docker compose up -d

## This is not needed anymore because is now done within compose.yaml
docker exec -it celery_worker bash
  - celery -A tasks worker -l INFO


## launch the celery app and run the python module
docker exec -it celery_app bash
  - python -m main

docker exec -it celery_send_task bash
  - python -m send_task

## Grafana
[flower docs](https://flower.readthedocs.io/en/latest/prometheus-integration.html#celery-flower-prometheus-grafana-integration-guide)
- add prometheus source
 + URL http//prometheus:9090
