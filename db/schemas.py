from pydantic import BaseModel, constr
from typing import List

class UserCreate(BaseModel):
    username: constr(min_length=5, max_length=10)


class Tweet(BaseModel):
    title: str
    text: str
    author_id: int

class UserBase(BaseModel):
    username: str
    registered_at: str
    tweets: List['Tweet']

class UsersGet(BaseModel):
    users: List[UserBase]

class Tweets(BaseModel):
    tweets: List[Tweet]

class TweetGet(BaseModel):
    id: int
