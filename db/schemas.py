from typing import Optional
from pydantic import BaseModel, constr

class UserCreate(BaseModel):
    username: constr(min_length=5, max_length=10)

class TweetCreate(BaseModel):
    title: str
    text: str
    author_id: int

class Tweet(TweetCreate):
    id: int

class TweetGet(BaseModel):
    id: int

class TweetUpdate(TweetGet):
    title: str
    text: str

class TweetPatch(TweetGet):
    title: str

class User(BaseModel):
    username: str
    tweets: list[Tweet]
    first_name: Optional[str]
    registered_at: Optional[str]

class UserShow(User):
    id: int

class UserDelete(BaseModel):
    id: int

class UserUpdate(BaseModel):
    id: int
    username: str
    first_name: str

class UserPatch(UserDelete):
    first_name: str

class Users(BaseModel):
    users: list[UserShow]

class Tweets(BaseModel):
    tweets: list[Tweet]