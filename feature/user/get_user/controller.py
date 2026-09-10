from fastapi import APIRouter, Header, Query, Path, Response
from .dto import GetUserParamsDto, GetUserQueryDto

router = APIRouter()
    
@router.get("/{user_id}")
def controller(query: GetUserQueryDto = Query(description="User name"), path: GetUserParamsDto = Path(description="User id")):
    return {"user_id": path.user_id, "status": "Success"}