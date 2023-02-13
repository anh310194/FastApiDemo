from pydantic import BaseModel


class Size(BaseModel):
    height: float
    length: float
    width: float
