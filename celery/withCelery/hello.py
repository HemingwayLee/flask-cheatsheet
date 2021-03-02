from celery import Celery

app = Celery('tasks', backend='redis://myredis', broker='redis://myredis')

@app.task
def add(x, y):
    return x + y
