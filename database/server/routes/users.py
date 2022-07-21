from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from bson.errors import InvalidId
from sympy import true

from database import (
    retrieve_user,
    retrieve_module,
    retrieve_modules,
    retrieve_users,
    add_user,
    update_user_module,
    delete_user,
    users,
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
    if len(user["userModules"]) == 0:
        user["userModules"] = {module["_id"]:module for module in retrieve_modules()}
    else:
        modules = {_id: retrieve_module(_id) for _id in user["userModules"]}
        user["userModules"] = modules

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

@router.get("/get_user_module", response_description="User module retrieved")
def get_user_module(userId, moduleId):
    try:
        user = retrieve_user(userId)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if user:
        try:
            module = user["userModules"][moduleId]
            return ResponseModel(module, "Module data retrieved successfully")
        except KeyError as e:
            return ErrorResponseModel("An error occured", 404, f"User does not contain module with id {moduleId}")


@router.get("/get_user_unit", response_description="User unit retrieved")
def get_user_unit(userId, moduleId, unitIndex: int):
    try:
        user = retrieve_user(userId)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if user:
        try:
            module = user["userModules"][moduleId]
            if unitIndex < len(module["units"]):
                unit = module["units"][unitIndex]
                return ResponseModel(unit, "Unit data retrieved successfully")
            else:
                return ErrorResponseModel("An eror occured", 404, "No unit exists")
        except KeyError as e:
            return ErrorResponseModel("An error occured", 404, f"User does not contain module with id {moduleId}")

@router.get("/get_user_module", response_description="User module retrieved")
def get_user_module(userId, moduleId):
    try:
        user = retrieve_user(userId)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if user:
        try:
            module = user["userModules"][moduleId]
            return ResponseModel(module, "Module data retrieved successfully")
        except KeyError as e:
            return ErrorResponseModel("An error occured", 404, f"User does not contain module with id {moduleId}")

@router.get("/user_exists")
def user_exists(userId):
    if(users.count_documents({"userId": userId}, limit=1)):
        user = retrieve_user(userId)
        return ResponseModel({"exists": True, "username" : user["username"]}, f"Counted documents with userId: {userId}")
    else:
         return ResponseModel({"exists": False}, f"Counted documents with userId: {userId}")
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
    module = user["userModules"][moduleId]
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
