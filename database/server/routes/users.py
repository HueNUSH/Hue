from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.errors import InvalidId

from database import (
    retrieve_user,
    retrieve_module,
    retrieve_users,
    add_user,
    update_user_module,
    delete_user,
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
    modules = {_id: retrieve_module(_id) for _id in user["attemptedModules"]}
    user["attemptedModules"] = modules

    new_user = add_user(user)
    return ResponseModel(new_user, "User added successfully")

@router.get("/get_users", response_description="Users retrieved")
def get_users():
    users = retrieve_users()
    if users:
        return ResponseModel(users, "Users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")

@router.get("/get_user", response_description="User retrieved")
def get_user(userId):
    try:
        user = retrieve_user(userId)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if user:
        return ResponseModel(user, "User data retrieved successfully")
    return ErrorResponseModel("An error occured", 404, "No user found")

@router.put("/update_user", response_description="User updated")
def update_user_data(userId, req: UpdateUsers = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}

    try:
        user = retrieve_user(userId)
        for k, v in req.items():
            user[k] = v
        user.pop("_id")

        updated_user = update_user(userId, user)

        if updated_module:
            return ResponseModel(
                f'User with ID: {userId} updated successfully',
                "Updated user successfully"
            )
        else:
            return ErrorResponseModel("An error occured", 400, "Unable to update user")
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")

@router.put("/complete_section", response_description="User section completed")
def complete_section(userId: str, moduleId: str, unit_index: int, section_index: int):
    user = retrieve_user(userId)
    module = user["attemptedModules"][moduleId]
    module["units"][unit_index]["sections"][section_index]["isComplete"] = True

    req = {k: v for k, v in module.items()}

    unitsCompleted = 0
    for unit in req["units"]:
        sectionsCompleted = 0
        for section in unit["sections"]:
            sectionsCompleted += section["isComplete"]
        unit["sectionsCompleted"] = sectionsCompleted

        unit_completed = sectionsCompleted == len(unit["sections"])
        unitsCompleted += unit_completed
        unit["isComplete"] = unit_completed

    req["unitsCompleted"] = unitsCompleted

    updated_user = update_user_module(userId, moduleId, req)
    if updated_user:
        return ResponseModel(
            f'User with ID: {userId} updated section complete successfully',
            "Updated user successfully"
        )
    else:
        return ErrorResponseModel("An error occured", 400, "Unable to update user")

@router.delete("/delete_user", response_description="User deleted")
def delete_user_data(userId: str):
    try:
        deleted_user = delete_user(userId)
        print(deleted_user)
        if deleted_user:
            return ResponseModel(
                f"User with ID: {userId} removed", "User deleted successfully"
            )
        else:
            return ErrorResponseModel("An error occured", 400, "Unable to delete user")
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
