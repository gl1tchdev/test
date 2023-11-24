from fastapi import APIRouter
from db import crud, schemas

users = APIRouter(prefix='/user')


@users.get('/all', response_model=schemas.Users)
async def get_users():
    user_list = crud.get_db_users()
    return {"users": user_list}

@users.get('/{user_id}', response_model=schemas.User)
async def get_user_by_id(user_id: int):
    user = crud.get_user_by_id(user_id)
    return user

@users.post('/', response_model=schemas.UserCreate)
async def register_user(user: schemas.UserCreate):
    db_user = crud.create_user(user)
    return db_user

@users.put('/', response_model=schemas.UserShow)
async def update(user: schemas.UserUpdate):
    db_user = crud.update_user(user)
    return db_user

@users.delete('/', response_model=schemas.UserShow)
async def delete_user(user: schemas.UserDelete):
    db_user = crud.delete_user(user)
    return db_user

@users.patch('/', response_model=schemas.UserShow)
async def set_first_name(user: schemas.UserPatch):
    db_user = crud.set_first_name(user)
    return db_user