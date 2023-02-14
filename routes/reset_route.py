from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from FastApiDemo.config.Database import resets_collection
from FastApiDemo.schemas.reset_schema import resets_serialize

reset_api_router = APIRouter(prefix="/reset", tags=["reset"])


@reset_api_router.get("/")
async def list_resets():
    result = resets_collection.find().to_list(100)
    return JSONResponse(status_code=status.HTTP_200_OK, content=resets_serialize(result))
