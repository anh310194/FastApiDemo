from pydantic import BaseModel, Field


class Size(BaseModel):
    height: float
    length: float
    width: float


class Inventory(BaseModel):
    item: str
    price: float
    size: Size
    qty: int
    features: str
    categories: list[str]
    image: str
