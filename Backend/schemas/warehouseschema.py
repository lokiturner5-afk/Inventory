from schemas.BaseSchema import BaseSchema
from pydantic import BaseModel



class WareHouseBase(BaseModel):
    name:str
    location: str

class WarehouseCreate(WareHouseBase):
    pass

class WarehouseRead(WareHouseBase, BaseSchema):
    id:int
