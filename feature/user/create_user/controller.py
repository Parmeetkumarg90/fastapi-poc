from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
        
@router.post("/items/")
def controller(item: Item):
    return {
        "item_name": item.name,
        "item_price": item.price,
        "message": "Item created successfully!"
    }