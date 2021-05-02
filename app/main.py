from datetime import timedelta

import uvicorn
from fastapi import FastAPI

from app.config import TIMEOUT
from app.redis_service import RedisClient
from app.schemas import Registration, Authorization, CodeReturn, ResultReturn
from app.utils.code_generator import generate_key

auth_app = FastAPI()


@auth_app.get("/")
async def root():
    """Initial endpoint"""
    return {"message": "Hello World"}


@auth_app.get("/get_code")
async def get_auth_code(
        user: Registration
):
    """Get code for authorization"""
    code = generate_key()
    redis = RedisClient()
    redis.client.setex(user.email, timedelta(seconds=TIMEOUT), code)
    return CodeReturn(code=code)


@auth_app.get("/auth")
async def auth(
        user: Authorization
):
    """Authorization by phone and code"""
    redis = RedisClient()
    code = redis.client.get(user.email)
    if code:
        if user.code == code.decode("utf-8"):
            return ResultReturn(result="success")
    return ResultReturn(result="error")


def run_auth_app():
    uvicorn.run(auth_app)


if __name__ == '__main__':
    run_auth_app()
