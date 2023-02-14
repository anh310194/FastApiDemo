from pydantic import BaseModel, Field


class CustomerAddress(BaseModel):
    country: str
    street1: str
    street2: str
    city: str
    state: str
    zip: str


class Customer(BaseModel):
    first_name: str
    last_name: str
    hashed_and_salted_password: str
    email_verified: bool
    address: CustomerAddress
    shipping_address: CustomerAddress | None = None


class CustomePost(Customer):
    email: str
