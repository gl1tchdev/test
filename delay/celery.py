from celery import Celery
from tweets.tasks import create_with_delay

app = Celery("delay",
             backend='rpc://',
             broker='amqp://guest:guest@localhost:5672//')
app.autodiscover_tasks()