from typing import List, Union
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse
from fastapi import APIRouter, status, HTTPException


from project.tasks import say_hello
from project.config import settings

router = APIRouter(prefix="/api")

@router.get("/{name}", status_code=status.HTTP_200_OK,
            response_class=PlainTextResponse,
            response_description="Greets a name")
async def greeter(name: Union[None, str] = None):

    task = say_hello.delay(name=name)
    output: str = task.get()

    return output


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

