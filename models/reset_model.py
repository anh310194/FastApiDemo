from datetime import datetime

from pydantic import BaseModel


class Reset(BaseModel):
    customer_id: str
    token: str
    status: str
    experation: datetime
    request_time: datetime
