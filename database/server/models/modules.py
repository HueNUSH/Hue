from typing import Literal

from pydantic import BaseModel, Field


# TODO : Validators for string length
class UnitSections(BaseModel):
    sectionId: int = Field(...)
    sectionName: str = Field(...)
    sectionSlug: str = Field(...)
    sectionDesc: str = Field(...)
    mediaType: Literal['pdf', 'html' 'video'] = Field(...)
    sectionMedia: str = Field(...)
    isComplete: bool = Field(...)


class Units(BaseModel):
    unitId: int = Field(...)
    unitName: str = Field(...)
    unitSlug: str = Field(...)
    unitDesc: str = Field(...)
    unitData: str = Field(...)
    sections: list[UnitSections] = Field(...)


class Modules(BaseModel):
    moduleId: int = Field(...)
    moduleName: str = Field(...)
    moduleSlug: str = Field(...)
    moduleDesc: str = Field(...)
    moduleData: str = Field(...)
    sections: list[UnitSections] = Field(...)


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
