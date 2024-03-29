from pydantic import BaseModel, Field


class Announcement(BaseModel):
    moduleId: str = Field(...)
    timestamp: str = Field(...)
    editedTimestamp: str = Field(...)
    title: str = Field(...)
    body: str = Field(...)


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
