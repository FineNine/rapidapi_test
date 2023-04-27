from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resent"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/")
async def read_items(item_id: int): # Declare api param types like this
    return {'item_id': item_id}

@app.get("/users/me") # Order matters, first path def will be used first
async def read_user_me():
    return {"user_id":"the current user"}

@app.get("users/{user_id}") # First path def of equal strings will be used
async def read_user(user_id: str):
    return {"user_id":user_id}
