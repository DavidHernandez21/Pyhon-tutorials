# from flask import Flask
# import boto3
from celery import Celery
import concurrent.futures



app = Celery('send_task', broker='amqp://guest:guest@rabbitmq:5672',
             backend='redis://redis:6379/0')


def wait_for_task(task_id: str, timeout: int) -> str:
    result = app.AsyncResult(task_id)
    if result.ready():
        return f"Result of the Task {result.get()}"
    print(f"Task is still running..waiting {timeout} seconds")
    try:
        return f"result from task {task_id} is {result.get(timeout=timeout)}"
    except celery.exceptions.TimeoutError:
        print("Task timed out")
        result.forget()
        return "Task timed out"

    

def call_method():
    print("Invoking Method ")
    r = app.send_task('tasks.add', kwargs={'first_number': 1, 'second_number': 2})
    print(r.backend)
    return r.id



def get_status(task_id: str) -> str:
    status = app.AsyncResult(task_id, app=app)
    print("Invoking Method ")
    if status.state == 'FAILURE':
        status.forget()
        return f"Task Failed with Exception: {status.info}"
    return f"Status of the Task {status.state}"



def task_result(task_id: str) -> str:
    result = app.AsyncResult(task_id)
    if result.ready():
        return f"Result of the Task {result.get()}"
    return "Task is still running"
    


def main():
    task_id = call_method()
    # print(type(task_id), task_id)
    task_id = task_id
    print(get_status(task_id=task_id))
    print(task_result(task_id=task_id))

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(wait_for_task, task_id, 5)
        print(future.result())
    


if __name__ == "__main__":
    main()
