from fastapi import APIRouter
from feature.user.get_user.controller import router as get_user_router
from feature.user.create_user.controller import router as create_user_router

user_router = APIRouter(prefix="/users", tags=["Users"])

user_router.include_router(get_user_router)
user_router.include_router(create_user_router)