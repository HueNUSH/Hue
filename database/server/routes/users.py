from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.errors import InvalidId

from database import (
    retrieve_user,
    retrieve_users,
    add_user,
)
from models.modules import (
    ErrorResponseModel,
    ResponseModel,
)
from models.users import (
    Users,
    UpdateUsers,
)

router = APIRouter()

@router.post("/create_user", response_description="User data added into database")
def create_user(user: Users = Body(...)):
    user = jsonable_encoder(user)
    new_user = add_user(user)
    return ResponseModel(new_user, "User added successfully")

@router.get("/get_users", response_description="Users retrieved")
def get_users():
    users = retrieve_users()
    if users:
        return ResponseModel(users, "Users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")

@router.get("/get_user/{id}", response_description="User retrieved")
def get_user(userId):
    try:
        user = retrieve_user(userId)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if user:
        return ResponseModel(user, "User data retrieved successfully")
    return ErrorResponseModel("An error occured", 404, "No user found")
