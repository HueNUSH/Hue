from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routes.modules import router as ModuleRouter
from routes.users import router as UserRouter
from routes.announcements import router as AnnouncementsRouter

app = FastAPI(title="HUE API",
              description="made by code monkeys :slight_smile:",
              version="0.1.0",
              docs_url='/chokola/docs',
              redoc_url='/chokola/redoc',
              openapi_url='/chokola/openapi.json')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ModuleRouter, tags=["Module"], prefix="/chokola/modules")
app.include_router(UserRouter, tags=["User"], prefix="/chokola/users")
app.include_router(AnnouncementsRouter, tags=["Announcements"], prefix="/chokola/announcements")

@app.get("/chokola/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
