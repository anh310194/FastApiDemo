from pydantic import BaseModel
from Models.size import Size


class Inventory(BaseModel):
    item: str
    price: float
    size: Size
    qty: int
    #features: list[str]
    image: str
