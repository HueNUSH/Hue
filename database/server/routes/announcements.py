from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from bson.errors import InvalidId
import pprint
from datetime import datetime
pp = pprint.PrettyPrinter(indent=4)
import auth

from database import (
    add_announcement,
    retrieve_announcement,
    retrieve_announcements,
    update_announcement,
    delete_announcement
)
from models.announcements import (
    ErrorResponseModel,
    ResponseModel,
    Announcement
)

router = APIRouter()

from fastapi.security import HTTPBearer  

token_auth_scheme = HTTPBearer()

@router.post("/create_announcement", response_description="Added announcement to the database")
def create_announcement(announcement: Announcement = Body(...), token : str = Depends(token_auth_scheme)):
    result = auth.VerifyToken(token.credentials).verify()
    if result.get("status"):
        return ErrorResponseModel("Bad request", 400, "You are unauthenticated!")

    announcement.timestamp = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
    announcement.editedTimestamp = ""
    announcement = jsonable_encoder(announcement)
    new_announcement = add_announcement(announcement)
    return ResponseModel(new_announcement, "Announcement added successfully")

@router.get("/get_announcements", response_description="Announcements retrieved")
def get_announcements():
    announcements = retrieve_announcements()
    if announcements:
        return ResponseModel(announcements, "Announcements retrieved successfully")
    return ResponseModel(announcements, "Empty list returned")

@router.get("/get_announcement", response_description="Announcement retrieved")
def get_announcement(announcement_id):
    try:
        announcement = retrieve_announcement(announcement_id)
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")
    if announcement:
        return ResponseModel(announcement, "Announcement retrieved successfully")
    return ErrorResponseModel("An error occured", 404, "No module found")

@router.put("/update_announcement", response_description="Announcement updated")
def update_announcement_data(announcement_id, req: Announcement = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}

    try:
        announcement = retrieve_announcement(announcement_id)
        for k, v in req.items():
            announcement[k] = v
        announcement.pop("_id")
        announcement['editedTimestamp'] = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
        updated_announcement = update_announcement(announcement_id, announcement)

        if updated_announcement:
            return ResponseModel(
                f'Announcement with ID: {announcement_id} updated successfully',
                "Updated announcement successfully"
            )
        else:
            return ErrorResponseModel("An error occured", 400, "Unable to update announcement")
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")

@router.delete("/delete_announcement", response_description="Announcement deleted from the database")
def delete_announcement_data(announcement_id: str):
    try:
        deleted_announcement = delete_announcement(announcement_id)
        if deleted_announcement:
            return ResponseModel(
                f"Module with ID: {announcement_id} removed", "Announcement deleted successfully"
            )
        else:
            return ErrorResponseModel("An error occured", 400, "Unable to delete announcement")
    except InvalidId as e:
        return ErrorResponseModel("An error occured", 404, "Invalid ID")

