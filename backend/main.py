from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from database import connect_to_database, execute_query

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# connect_to_database()
# get = execute_query()
# print(get)

@app.get("/")
def read_root():
    result = execute_query()
    return result


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}