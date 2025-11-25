from typing import  Optional
from pydantic import  EmailStr
from schemas.BaseSchema import BaseSchema
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name:str
    email:Optional[EmailStr] = None
    phone:str
    address:str
    customer_type:str = "single"


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase, BaseSchema):
    id: int