from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    retrieve_module,
    retrieve_module,
    add_module
)
from models.modules import (
    ErrorResponseModel,
    ResponseModel,
    Modules
)

router = APIRouter()


@router.post("/create_module", response_description="Module data added into database")
def create_module(module: Modules = Body(...)):
    module = jsonable_encoder(module)
    new_module = add_module(module)
    return ResponseModel(new_module, "Module added successfully")
