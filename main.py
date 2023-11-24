from fastapi import FastAPI
from users.routes import users
from tweets.routes import tweets


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(users)
    app.include_router(tweets)
    return app



app = create_app()

@app.get('/')
async def welcome():
    return {'message': 'hello'}