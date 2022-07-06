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
users = database.users_collection
announcements = database.announcements_collection
schedule = database.schedule_collection


# General helper functions
def retrieve_objects(objCollection) -> list:
    objList = []
    for obj in objCollection.find():
        obj["_id"] = str(obj["_id"])
        objList.append(obj)
    return objList

def retrieve_object(objId, objCollection) -> dict:
    obj = objCollection.find_one({"_id": objId})
    if obj:
        obj["_id"] = str(obj["_id"])
    return obj

def add_object(objData: dict, objCollection) -> dict:
    objId = objCollection.insert_one(objData).inserted_id
    obj = objCollection.find_one({"_id": objId})

    # Convert ObjectId back to str as FastApi can't parse it
    obj["_id"] = str(obj["_id"])
    return obj

def update_obj(objId, objData: dict, objCollection) -> bool:
    obj = objCollection.find_one({"_id": objId})

    # Convert ObjectID back to str as FastAPI can't parse it
    obj["_id"] = str(obj["_id"])

    if obj:
        result = objCollection.update_one({'_id': ObjectId(objId)}, {"$set" : objData })

        if result:
            return True

    return False

def delete_obj(objId, objCollection) -> bool:
    obj = objCollection.find_one({"_id": ObjectId(objId)})

    if obj:
        objCollection.delete_one({"_id": ObjectId(objId)})
        return True
    return False


# CRUD Operations for modules
def retrieve_modules():
    return retrieve_objects(modules)

def retrieve_module(moduleId: str):
    return retrieve_object(ObjectId(moduleId), modules)

def add_module(moduleData: dict):
    return add_object(moduleData, modules)

def update_module(moduleId: str, moduleData: dict):
    return update_obj(ObjectId(moduleId), moduleData, modules)

def delete_module(moduleId: str):
    delete_object(ObjectId(moduleId), modules)


# CRUD Operations for users
def add_user(userData: dict):
    return add_object(userData, users)

def retrieve_users():
    return retrieve_objects(users)

def retrieve_user(userId: str):
    user = users.find_one({"userId": userId})
    user["_id"] = str(user["_id"])
    return user

