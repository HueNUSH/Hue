from typing import Literal, Optional
from pydantic import BaseModel, Field
from models.modules import (
    ErrorResponseModel,
    ResponseModel,
    Modules
)


class Users(BaseModel):
    username: str = Field(...)
    userId: str = Field(...)
    createdAt: int = Field(...)
    email: str = Field(...)
    isAdmin: Optional[bool] = False #Default false
    attemptedModules: Optional[list[Modules]] = None #Default no attempted modules

class UpdateUsers:
    username: Optional[str]
    userId: Optional[str]
    createdAt: Optional[int]
    email: Optional[str]
    isAdmin: Optional[bool]
    attemptedModules: Optional[list[Modules]]
