from schemas.BaseSchema import BaseSchema
from typing import Optional, List
from decimal import Decimal
from schemas.purchaseItemschema import PurchaseItemCreate
from pydantic import BaseModel

class PurchaseBase(BaseModel):
    supplier_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    total_amount: Decimal = 0
    status: str = "completed"
    reference: Optional[str] = None


class PurchaseCreate(PurchaseBase):
    purchase_items : Optional[List[PurchaseItemCreate]] = None


class PurchaseRead(PurchaseBase, BaseSchema):
    id: int
