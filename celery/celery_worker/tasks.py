import random
import time

from celery import Celery

# from celery.utils.log import get_task_logger

# logger = get_task_logger(__name__)

# app = Celery('tasks', broker='amqp://guest:guest@rabbitmq:5672',
#              backend='redis://redis:6379/0')
app = Celery("tasks")
app.config_from_object("celeryconfig")


@app.task
def add(first_number: int | float, second_number: int | float) -> int | float:
    # logger.info('Got Request - Starting work ')
    time.sleep(random.randint(1, 4))
    # logger.info('Work Finished ')
    return first_number + second_number
