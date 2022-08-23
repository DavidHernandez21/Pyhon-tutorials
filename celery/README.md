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

## flower
great resource thats explain gotchas about tracking more than one celery worker with flower [link](https://www.distributedpython.com/2018/10/13/flower-docker/#:~:text=Celery%20is%20a%20marshland%20plant%20in%20the%20family,in%20Computer%20Science%3A%20cache%20invalidation%20and%20naming%20things.)
- tldr: using the `--hostname` worker option

## Dockle - Container Image Linter for Security, Helping build the Best-Practice Docker Image
- export DOCKLE_LATEST=$(curl --silent "https://api.github.com/repos/goodwithtech/dockle/releases/latest" | jq .tag_name | sed  's/"//g')
- docker run --rm -v /var/run/docker.sock:/var/run/docker.sock goodwithtech/dockle:${DOCKLE_LATEST} `image_name`
