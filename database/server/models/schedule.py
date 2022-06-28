from pydantic import BaseModel, Field


# TODO : Validator for event name length
class Schedule(BaseModel):
    moduleId: int = Field(...)
    start: int = Field(...)
    end: int = Field(...)
    eventName: str = Field(...)


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
