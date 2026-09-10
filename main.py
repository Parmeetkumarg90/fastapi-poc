from fastapi import FastAPI
from feature.user.user_router import user_router

app = FastAPI(title="My fastapi poc")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

app.include_router(user_router)