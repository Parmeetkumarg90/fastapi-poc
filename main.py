from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My fastapi poc")

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
    
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "status": "Success"}
    
@app.post("/items/")
def create_item(item: Item):
    return {
        "item_name": item.name,
        "item_price": item.price,
        "message": "Item created successfully!"
    }