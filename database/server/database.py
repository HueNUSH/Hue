from bson.objectid import ObjectId
from pymongo import MongoClient

from models.modules import (
    ErrorResponseModel,
    ResponseModel,
    Modules
)

from models.users import (
    Users
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

def retrieve_object(objId, objCollection, idKey = "_id") -> dict:
    obj = objCollection.find_one({idKey: objId})
    if obj:
        obj["_id"] = str(obj["_id"])
    return obj

def add_object(objData: dict, objCollection) -> dict:
    objId = objCollection.insert_one(objData).inserted_id
    obj = objCollection.find_one({"_id": objId})

    # Convert ObjectId back to str as FastApi can't parse it
    obj["_id"] = str(obj["_id"])
    return obj

def update_obj(objId, objData: dict, objCollection, idKey = "_id") -> bool:
    obj = objCollection.find_one({idKey: objId})

    # Convert ObjectID back to str as FastAPI can't parse it
    obj["_id"] = str(obj["_id"])
    if obj:
        result = objCollection.update_one({idKey: objId}, {"$set" : objData })

        if result:
            return True

    return False

def delete_obj(objId, objCollection, idKey = "_id") -> bool:
    obj = objCollection.find_one({idKey: objId})
    print(obj)

    if obj:
        objCollection.delete_one({idKey: objId})
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
    delete_obj(ObjectId(moduleId), modules)


# CRUD Operations for users
def add_user(userData: dict):
    return add_object(userData, users)

def retrieve_users():
    return retrieve_objects(users)

def retrieve_user(userId: str):
    return retrieve_object(userId, users, idKey = "userId")

def update_user(userId: str, userData: dict):
    return update_obj(userId, userData, users, idKey = "userId")

def update_user_module(userId: str, moduleId, moduleData: dict):
    return update_obj(userId, {f"userModules.{moduleId}": moduleData}, users, idKey = "userId")

def delete_user(userId):
    return delete_obj(userId, users, idKey = "userId")

# CRUD Operations for announcements
def retrieve_announcements():
    return retrieve_objects(announcements)

def retrieve_announcement(announcementId : str):
    return retrieve_object(ObjectId(announcementId), announcements)

def add_announcement(announcementData : dict):
    return add_object(announcementData,announcements)

def update_announcement(announcementId : str, announcementData : dict):
    return update_obj(ObjectId(announcementId), announcementData, announcements)

def delete_announcement(announcementId : str):
    delete_obj(ObjectId(announcementId),announcements)
