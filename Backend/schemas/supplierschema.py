from typing import  Optional
from pydantic import  EmailStr
from schemas.BaseSchema import BaseSchema
from pydantic import BaseModel

class SupplierBase(BaseModel):
    name:str
    contact_person:Optional[str] = None
    email:Optional[EmailStr] = None
    phone:str
    address:str

class SupplierCreate(SupplierBase):
    pass

class SupplierRead(SupplierBase, BaseSchema):
    id:int