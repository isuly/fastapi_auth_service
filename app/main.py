import uvicorn
from fastapi import FastAPI

auth_app = FastAPI()


@auth_app.get("/")
async def root():
    return {"message": "Hello World"}


def run_auth_app():
    uvicorn.run(auth_app)


if __name__ == '__main__':
    run_auth_app()
