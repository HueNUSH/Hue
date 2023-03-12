from typing import Literal, Optional, List
from pydantic import BaseModel, Field


# TODO : Validators for string length
class UnitSections(BaseModel):
    sectionName: str = Field(...)
    sectionDesc: str = Field(...)
    mediaType: Literal['pdf', 'embed', 'slides'] = Field(...)
    sectionMedia: str = Field(...)
    sectionIcon: str = Field(...)
    isComplete: bool = False

class Units(BaseModel):
    unitName: str = Field(...)
    unitDesc: str = Field(...)
    unitAbout: str = Field(...)
    sections: List[UnitSections] = Field(...)
    sectionsCompleted: int = 0
    sectionProgress: List[int] = Field(...)
    isComplete: bool = False

class Modules(BaseModel):
    moduleName: str = Field(...)
    moduleDesc: str = Field(...)
    moduleAbout: str = Field(...)
    moduleIcon: str = Field(...)
    moduleIconBackgroundColor: str = Field(...)
    units: List[Units] = Field(...)
    unitsCompleted: int = 0

class UpdateSections(BaseModel):
    sectionName: Optional[str]
    sectionDesc: Optional[str]
    mediaType: Optional[Literal['pdf', 'embed', 'slides']]
    sectionMedia: Optional[str]
    sectionIcon: Optional[str]

class UpdateUnits(BaseModel):
    unitName: Optional[str]
    unitDesc: Optional[str]
    unitAbout: Optional[str]
    sections: Optional[List[UpdateSections]]

class UpdateModules(BaseModel):
    moduleName: Optional[str]
    moduleDesc: Optional[str]
    moduleAbout: Optional[str]
    moduleIcon: Optional[str]
    moduleIconBackgroundColor: Optional[str]
    units: Optional[List[UpdateUnits]]




def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
