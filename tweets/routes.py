from fastapi import APIRouter
from db import schemas, crud
from .tasks import create_with_delay

tweets = APIRouter(prefix='/tweet')


@tweets.get('/get', response_model=schemas.Tweets)
async def get_all_tweets():
    tweets = crud.get_tweets()
    return {'tweets': tweets}

@tweets.get('/get/{tweet_id}', response_model=schemas.Tweets)
async def get_tweet(tweet_id: int):
    db_tweet = crud.get_tweet_by_id(tweet_id)
    return db_tweet

@tweets.put('/', response_model=schemas.Tweet)
async def create_tweet(tweet: schemas.Tweet):
    db_tweet = crud.create_tweet(tweet)
    return db_tweet

@tweets.delete('/', response_model=schemas.Tweet)
async def delete_tweet(tweet: schemas.TweetGet):
    db_tweet = crud.delete_tweet(tweet)
    return db_tweet

@tweets.post('/{delay}')
async def tweet_with_delay(tweet: schemas.Tweet, delay: int):
    data = [tweet.title, tweet.text, tweet.author_id]
    create_with_delay.delay(data, delay)
    return {"delay": delay}