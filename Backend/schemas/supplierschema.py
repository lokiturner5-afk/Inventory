from typing import  Optional
from pydantic import  EmailStr
from schemas.BaseSchema import BaseSchema

class SupplierBase(BaseSchema):
    name:str
    contact_person:Optional[str] = None
    email:Optional[EmailStr] = None
    phone:str
    address:str

class SupplierCreate(SupplierBase):
    pass

class SupplierRead(SupplierBase):
    id:int