from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse, Response
from FastApiDemo.config.Database import customers_collection
from FastApiDemo.models.customer_model import Customer, CustomePost
from FastApiDemo.schemas.customer_schema import customers_serializer, customer_serializer

customer_api_router = APIRouter(prefix="/customer", tags=["Customer"])


@customer_api_router.get("/")
async def list_customers():
    customers = await customers_collection.find().to_list(100)
    return JSONResponse(status_code=status.HTTP_200_OK, content=customers_serializer(customers))


@customer_api_router.get("/{email}")
async def list_customers(email: str):
    customer = await customers_collection.find_one({"_id": email})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=customer_serializer(customer))


@customer_api_router.post("/")
async def add_new_customer(model: CustomePost = Body()):
    customer = jsonable_encoder(model, exclude=["email"])
    customer["_id"] = model.email
    new_customer = await customers_collection.insert_one(customer)
    created_customer = await customers_collection.find_one({"_id": new_customer.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=customer_serializer(created_customer))


@customer_api_router.put("/{email}")
async def update_customer(email: str, model: Customer = Body()):
    customer_encoder = jsonable_encoder(model, exclude=["email"])
    update_customer = await customers_collection.update_one({"_id": email}, {"$set": customer_encoder} )
    if update_customer.modified_count == 1:
        updated_customer = await customers_collection.find_one({"_id": email})
        if updated_customer is not None:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content=customer_serializer(updated_customer))
    return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"inventory {id} do not be update")
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=customer_serializer(customer))


@customer_api_router.delete("/{email}")
async def delete_customer(email: str):
    result = await customers_collection.delete_one({"_id": email})
    if result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Student {id} not found")