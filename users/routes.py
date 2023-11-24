from fastapi import APIRouter
from db.schemas import UsersGet, UserCreate, UserBase
from db.crud import *

users = APIRouter(prefix='/user')


@users.get('/get', response_model=UsersGet)
async def get_users():
    user_list = get_db_users()
    return {"users": user_list}

@users.get('/get/{user_id}', response_model=UserBase)
async def user_by_id(user_id: int):
    user = get_user_by_id(user_id)
    return user

@users.get('/get/{username}', response_model=UserBase)
async def user_by_username(username: str):
    user = get_user_by_username(username)
    return user

@users.post('/', response_model=UserCreate)
async def register(user: UserCreate):
    db_user = create_user(user)
    return db_user


@users.delete('/', response_model=UserCreate)
async def del_user(user: UserCreate):
    db_user = delete_user(user)
    return db_user