from bson.objectid import ObjectId
from pymongo import MongoClient

from models.modules import (
    ErrorResponseModel,
    ResponseModel,
    Modules
)

MONGO_DETAILS = "mongodb://localhost:27017"

client = MongoClient(MONGO_DETAILS)

database = client.database

modules = database.modules_collection
announcements = database.announcements_collection
schedule = database.schedule_collection


# CRUD Operations

# Get all modules
def retrieve_modules() -> list:
    moduleList = []
    for module in modules.find():
        moduleList.append(module)
    return moduleList

# Get a module
def retrieve_module(moduleId: str) -> dict:
    module = modules.find_one({"_id": ObjectId(moduleId)})
    if module:
        return module


# Add a module
def add_module(module_data: dict) -> dict:
    module_id = modules.insert_one(module_data).inserted_id
    module = modules.find_one({"_id": module_id})

    # Convert ObjectID back to str as FastAPI can't parse it
    module["_id"] = str(module["_id"])
    print(module["units"][0])
    return module
