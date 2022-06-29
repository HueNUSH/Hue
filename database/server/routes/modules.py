from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.errors import InvalidId

from database import (
    retrieve_modules,
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
    print(module.units)
    module = jsonable_encoder(module)
    new_module = add_module(module)
    return ResponseModel(new_module, "Module added successfully")

@router.get("/get_modules", response_description="Modules retrieved")
def get_modules():
    modules = retrieve_modules()
    if modules:
        return ResponseModel(modules, "Modules data retrieved successfully")
    return ResponseModel(modules, "Empty list returned")

@router.get("/get_module/{id}", response_description="Module retrieved")
def get_module(module_id):
    try:
        module = retrieve_module(module_id)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if module:
        return ResponseModel(module, "Module data retrieved successfully")
    return ErrorResponseModel("An error occured", 404, "No module found")
