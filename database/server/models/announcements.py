from pydantic import BaseModel, Field


class Announcement(BaseModel):
    moduleId: int = Field(...)
    timestamp: int = Field(...)
    title: str = Field(...)
    data: str = Field(...)
