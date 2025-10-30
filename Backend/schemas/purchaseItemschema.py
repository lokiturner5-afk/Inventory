
from schemas.BaseSchema import BaseSchema
from decimal import Decimal

class PurchaseItemBase(BaseSchema):
    purchase_id: int
    item_id: int
    quantity: int
    unit_cost: Decimal


class PurchaseItemCreate(PurchaseItemBase):
    pass


class PurchaseItemRead(PurchaseItemBase):
    id: int
