import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.database

modules = database.get_collection("modules_collection")
announcements = database.get_collection("announcements_collection")
schedule = database.get_collection("schedule_collection")
