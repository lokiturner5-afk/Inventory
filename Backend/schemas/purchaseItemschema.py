
from schemas.BaseSchema import BaseSchema
from decimal import Decimal
from pydantic import BaseModel

class PurchaseItemBase(BaseModel):
    purchase_id: int
    item_id: int
    quantity: int
    unit_cost: Decimal


class PurchaseItemCreate(PurchaseItemBase):
    pass


class PurchaseItemRead(PurchaseItemBase, BaseSchema):
    id: int
