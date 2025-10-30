from typing import  Optional
from pydantic import  EmailStr
from schemas.BaseSchema import BaseSchema


class CustomerBase(BaseSchema):
    name:str
    email:Optional[EmailStr] = None
    phone:str
    address:str
    customer_type:str = "single"


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    id: int