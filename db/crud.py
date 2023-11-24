from sqlalchemy.orm import Session, create_session
from sqlalchemy import select, create_engine
from config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME
from db.models import User, Tweet
from db import schemas


db_url = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(db_url)

session_db: Session = create_session(bind=engine)

def get_db_users() -> list[User]:
    query = select(User)
    result = session_db.execute(query)
    return result.scalars().all()

def get_user_by_username(nickname: str) -> User:
    query = select(User).where(User.username == nickname)
    return session_db.execute(query).scalar_one()

def get_user_by_id(user_id: int) -> User:
    query = select(User).where(User.id == user_id)
    return session_db.execute(query).scalar_one()

def create_user(user_data: schemas.UserCreate) -> User:
    db_user = User(username=user_data.username)
    session_db.add(db_user)
    session_db.commit()
    return db_user

def delete_user(user_data: schemas.UserCreate) -> User:
    query = select(User).where(User.username == user_data.username)
    result = session_db.execute(query).scalar()
    session_db.delete(result)
    session_db.commit()
    return result

def get_tweets() -> list[Tweet]:
    query = select(Tweet)
    result = session_db.execute(query)
    return result.scalars().all()

def get_tweet_by_id(tweet_id: int) -> Tweet:
    query = select(Tweet).where(Tweet.id == tweet_id)
    return session_db.execute(query).scalar_one()

def create_tweet(tweet: schemas.Tweet) -> Tweet:
    db_tweet = Tweet(text=tweet.text, title=tweet.title, author_id=tweet.author_id)
    session_db.add(db_tweet)
    session_db.commit()
    return db_tweet

def delete_tweet(tweet: schemas.TweetGet) -> Tweet:
    query = select(Tweet).where(Tweet.id == tweet.id)
    result = session_db.execute(query).scalar()
    session_db.delete(result)
    session_db.commit()
    return result

