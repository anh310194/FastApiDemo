import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["e_commerce"]
inventories_collection = db["inventories"]
customers_collection = db["customers"]
resets_collection = db["resets"]