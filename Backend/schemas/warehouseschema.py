from schemas.BaseSchema import BaseSchema



class WareHouseBase(BaseSchema):
    name:str
    location: str

class WarehouseCreate(WareHouseBase):
    pass

class WarehouseRead(WareHouseBase):
    id:int
