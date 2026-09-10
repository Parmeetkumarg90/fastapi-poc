from pydantic import BaseModel

class GetUserParamsDto(BaseModel):
    user_id: int

class GetUserQueryDto(BaseModel):
    name: str | None = None