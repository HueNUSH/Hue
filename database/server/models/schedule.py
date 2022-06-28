from pydantic import BaseModel, Field


# TODO : Validator for event name length
class Schedule(BaseModel):
    moduleId: int = Field(...)
    start: int = Field(...)
    end: int = Field(...)
    eventName: str = Field(...)
