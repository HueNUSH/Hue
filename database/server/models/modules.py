from typing import Literal, Optional
from pydantic import BaseModel, Field


# TODO : Validators for string length
class UnitSections(BaseModel):
    sectionName: str = Field(...)
    sectionDesc: str = Field(...)
    mediaType: Literal['pdf', 'html' 'video'] = Field(...)
    sectionMedia: str = Field(...)
    isComplete: bool = False

class Units(BaseModel):
    unitName: str = Field(...)
    unitDesc: str = Field(...)
    unitAbout: str = Field(...)
    sections: list[UnitSections] = Field(...)
    sectionsCompleted: int = 0
    isComplete: bool = False

class Modules(BaseModel):
    moduleName: str = Field(...)
    moduleDesc: str = Field(...)
    moduleAbout: str = Field(...)
    moduleIcon: str = Field(...)
    moduleIconBackgroundColor: str = Field(...)
    units: list[Units] = Field(...)
    unitsCompleted: int = 0

class UpdateSections(BaseModel):
    sectionName: Optional[str]
    sectionDesc: Optional[str]
    mediaType: Optional[Literal['pdf', 'html' 'video']]
    sectionMedia: Optional[str]
    isComplete: Optional[bool]

class UpdateUnits(BaseModel):
    unitName: Optional[str]
    unitDesc: Optional[str]
    unitAbout: Optional[str]
    sections: Optional[list[UpdateSections]]

class UpdateModules(BaseModel):
    moduleName: Optional[str]
    moduleDesc: Optional[str]
    moduleAbout: Optional[str]
    moduleIcon: Optional[str]
    moduleIconBackgroundColor: Optional[str]
    units: Optional[list[UpdateUnits]]




def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
