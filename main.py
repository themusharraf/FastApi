from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/post")
# async def say_hello(payload: dict = Body(...)):
#     return {"message": payload["message"]}
