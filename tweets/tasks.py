from celery import shared_task
from db import crud, schemas
from time import sleep

@shared_task()
def create_with_delay(data: dict, delay: int):
    sleep(delay)
    tweet = schemas.Tweet(title=data[0], text=data[1], author_id=data[2])
    crud.create_tweet(tweet)
