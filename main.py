import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

from FastApiDemo.routes.customer_route import customer_api_router
from FastApiDemo.routes.inventory_route import inventory_api_router
from FastApiDemo.routes.reset_route import reset_api_router

app = FastAPI(docs_url=None)
app.mount("/assets", StaticFiles(directory="assets"), name="static")

# add router
app.include_router(inventory_api_router)
app.include_router(customer_api_router)
app.include_router(reset_api_router)


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title='Gigarion Swagger',
        swagger_favicon_url="/assets/logo/icon.jpg"
    )

if __name__ == "__main__":
    uvicorn.run(app)
