from typing import Literal, Optional, List
from pydantic import BaseModel, Field
from models.modules import (
    ErrorResponseModel,
    ResponseModel,
    Modules
)

class Users(BaseModel):
    userId: str = Field(...)
    username: str = Field(...)
    createdAt: int = Field(...)
    email: str = Field(...)
    userModules: List[str] = [] #Default no attempted modules

class UpdateUsers(BaseModel):
    username: Optional[str]
    userId: Optional[str]
    createdAt: Optional[int]
    email: Optional[str]
