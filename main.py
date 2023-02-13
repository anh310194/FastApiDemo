import uvicorn
from fastapi import FastAPI, Body, status, HTTPException
from Database import db
from fastapi.responses import JSONResponse, Response
from Models.inventory import Inventory
from fastapi.encoders import jsonable_encoder
from Schema.inventory_schema import inventories_serializer, inventory_serializer
from bson import ObjectId

app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


@app.get("/inventory/")
async def list_inventories():
    result = await db.inventories.find().to_list(1000)
    inventories = inventories_serializer(result)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=inventories)


@app.post("/inventory/")
async def add_new_inventory(model: Inventory):
    inventory = jsonable_encoder(model)
    new_inventory = await db.inventories.insert_one(inventory)
    created_inventory = await db.inventories.find_one({"_id": new_inventory.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=inventory_serializer(created_inventory))


@app.get("/inventory/{id}")
async def get_inventory(id: str):    
    inventory = await db.inventories.find_one({"_id": ObjectId(id)})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=inventory_serializer(inventory))


@app.delete("/inventory/{id}")
async def delete_inventory(id: str):
    result = await db.inventories.delete_one({"_id": ObjectId(id)})
    
    if result.deleted_count == 1:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Student {id} not found")

if __name__ == "__main__":
    uvicorn.run(app)
