references [this](https://github.com/veryacademy/YT_FastAPI_Celery_Redis_Flower_Introduction) and [another one](https://github.com/soumilshah1995/Python-Flask-Redis-Celery-Docker)

celery [documentation](https://docs.celeryq.dev/en/stable/index.html)

docker compose up -d

docker exec -it celery_worker bash
 - celery -A tasks worker -l INFO

 docker exec -it celery_app bash
  - python main.py

docker exec -it celery_send_task bash
 - python send_task.py
