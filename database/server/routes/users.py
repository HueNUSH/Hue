from fastapi import APIRouter, Body, Query
from fastapi.encoders import jsonable_encoder
from bson.errors import InvalidId

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


def create_user_progress(module_id: str):
    unitProgress = []
    for index, unit in enumerate(retrieve_module(module_id)["units"]):
        sectionProgress = [0 for _ in range(len(unit["sections"]))]

        unitProgress.append({
                "sectionsCompleted": 0,
                "sectionProgress": sectionProgress
            })

    return {
            "unitsCompleted": 0,
            "unitProgress": unitProgress
            }

@router.post("/create_user", response_description="User data added into database")
def create_user(user: Users = Body(...)):
    user = jsonable_encoder(user)

    modules = {}
    for _id in user["userModules"]:
        modules[_id] = create_user_progress(_id)

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
def get_user(userId: str):
    try:
        user = retrieve_user(userId)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if user:
        return ResponseModel(user, "User data retrieved successfully")
    return ErrorResponseModel("An error occured", 404, "No user found")

@router.get("/get_user_module", response_description="User module retrieved")
def get_user_module(userId: str, moduleId: str):
    try:
        user = retrieve_user(userId)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if user:
        if moduleId in user["userModules"]:
            module = retrieve_module(module)

            return ResponseModel(module, "Module data retrieved successfully")
        else:
            return ErrorResponseModel("An error occured", 404, f"User does not contain module with id {moduleId}")


@router.get("/get_user_unit", response_description="User unit retrieved")
def get_user_unit(userId: str, moduleId: str, unitIndex: int):
    try:
        user = retrieve_user(userId)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if user:
        if moduleId in user["userModules"]:
            module = retrieve_module(moduleId)
            if unitIndex < len(module["units"]):
                unit = module["units"][unitIndex]

                return ResponseModel(unit, "Unit data retrieved successfully")
            else:
                return ErrorResponseModel("An error occured", 404, "No unit exists")
        else:
            return ErrorResponseModel("An error occured", 404, f"User does not contain module with id {moduleId}")

@router.get("/user_exists")
def user_exists(userId: str):
    if(users.count_documents({"userId": userId}, limit=1)):
        user = retrieve_user(userId)
        return ResponseModel({"exists": True, "username" : user["username"]}, f"Counted documents with userId: {userId}")
    else:
         return ResponseModel({"exists": False}, f"Counted documents with userId: {userId}")
@router.put("/update_user", response_description="User updated")
def update_user_data(userId: str, req: UpdateUsers = Body(...)):
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
def complete_section(userId: str, moduleId: str, unit_index: int = Query(default = None, ge=0), section_index: int = Query(default = None, ge=0)):
    user = retrieve_user(userId)

    if moduleId in user["userModules"]:
        moduleProgress = user["userModules"][moduleId]

        if not unit_index < len(moduleProgress["unitProgress"]):
            return ErrorResponseModel("An error occured", 404, "No unit found")
        unit = moduleProgress["unitProgress"][unit_index]

        if not section_index < len(unit["sectionProgress"]):
            return ErrorResponseModel("An error occured", 404, "No section found")

        # Just in case this endpoint is called on a completed section
        if not unit["sectionProgress"][section_index]:
            unit["sectionProgress"][section_index] = 1
            unit["sectionsCompleted"] = unit["sectionProgress"].count(1)
            if unit["sectionsCompleted"] == len(unit["sectionProgress"]):
                moduleProgress["unitsCompleted"] += 1
    else:
        try:
            module = retrieve_module(moduleId)
            if module:
                user["userModules"][moduleId] = create_user_progress(moduleId)

                update_user_module(userId, moduleId, user["userModules"][moduleId])
                # Recursive function yooooo
                return complete_section(userId, moduleId, unit_index, section_index)
            else:
                return ErrorResponseModel("An error occured", 404, f"Module with id {moduleId} not found")
        except InvalidId as e:
            return ErrorResponseModel("An error occured", 404, "Invalid ID")


    updated_user = update_user_module(userId, moduleId, user["userModules"][moduleId])
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
