import uvicorn
from fastapi import FastAPI

auth_app = FastAPI()


@auth_app.get("/")
async def root():
    """Initial endpoint"""
    return {"message": "Hello World"}


@auth_app.get("/get_code")
async def get_auth_code():
    """Get code for authorization"""
    pass


@auth_app.get("/auth")
async def auth():
    """Authorization by phone and code"""
    pass


def run_auth_app():
    uvicorn.run(auth_app)


if __name__ == '__main__':
    run_auth_app()
