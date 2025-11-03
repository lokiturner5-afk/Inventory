from schemas.BaseSchema import BaseSchema
from decimal import Decimal
from pydantic import BaseModel

class SaleItemBase(BaseModel):
    sale_id: int
    item_id: int
    quantity: int
    unit_price: Decimal


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemRead(SaleItemBase, BaseSchema):
    id: int

