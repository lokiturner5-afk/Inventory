from schemas.BaseSchema import BaseSchema
from decimal import Decimal

class SaleItemBase(BaseSchema):
    sale_id: int
    item_id: int
    quantity: int
    unit_price: Decimal


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemRead(SaleItemBase):
    id: int

