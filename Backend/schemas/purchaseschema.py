from schemas.BaseSchema import BaseSchema
from typing import Optional, List
from decimal import Decimal
from schemas.purchaseItemschema import PurchaseItemCreate


class PurchaseBase(BaseSchema):
    supplier_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    total_amount: Decimal = 0
    status: str = "completed"
    reference: Optional[str] = None


class PurchaseCreate(PurchaseBase):
    purchase_items = Optional[List[PurchaseItemCreate]]


class PurchaseRead(PurchaseBase):
    id: int
