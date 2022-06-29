from typing import Literal, Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, Field


# TODO : Validators for string length
class UnitSections(BaseModel):
    sectionName: str = Field(...)
    sectionSlug: str = Field(...)
    sectionDesc: str = Field(...)
    mediaType: Literal['pdf', 'html' 'video'] = Field(...)
    sectionMedia: str = Field(...)
    isComplete: bool = Field(...)


class Units(BaseModel):
    unitName: str = Field(...)
    unitSlug: str = Field(...)
    unitDesc: str = Field(...)
    unitData: str = Field(...)
    sections: list[UnitSections] = Field(...)


class Modules(BaseModel):
    moduleName: str = Field(...)
    moduleSlug: str = Field(...)
    moduleDesc: str = Field(...)
    moduleData: str = Field(...)
    units: list[Units] = Field(...)

class UpdateModules(BaseModel):
    moduleName: Optional[str]
    moduleSlug: Optional[str]
    moduleDesc: Optional[str]
    moduleData: Optional[str]
    units: Optional[list[Units]]


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
