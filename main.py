from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import json

def load_json(filepath: str):
    with open(filepath) as file:
        json_file = json.loads(f)
    return json_file

app = FastAPI()




# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {'item_id': item_id, "q": q}
#     return {'item_id': item_id}

# 
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
    # return fake_items_db[skip:skip+limit]
# 
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resent"
#     lenet = "lenet"

# app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"message": "Hello World"}

# @app.get("/")
# async def read_items(item_id: int): # Declare api param types like this
#     return {'item_id': item_id}

# @app.get("/users/me") # Order matters, first path def will be used first
# async def read_user_me():
#     return {"user_id":"the current user"}

# @app.get("users/{user_id}") # First path def of equal strings will be used
# async def read_user(user_id: str):
#     return {"user_id":user_id}

