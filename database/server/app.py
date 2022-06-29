from fastapi import FastAPI
import uvicorn

from routes.modules import router as ModuleRouter

app = FastAPI()

app.include_router(ModuleRouter, tags=["Module"], prefix="/modules")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
