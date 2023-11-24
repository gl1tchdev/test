from celery import Celery

app = Celery("delay",
             backend='rpc://',
             broker='amqp://guest:guest@localhost:5672//')
app.autodiscover_tasks()