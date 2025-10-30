from schemas.BaseSchema import BaseSchema
from typing import Optional, List
from decimal import Decimal
from schemas.saleitemBase import SaleItemCreate

class SaleBase(BaseSchema):
    customer_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    sale_type: Optional[str] = None
    total_amount: Decimal = 0
    status: str = "completed"
    reference: Optional[str] = None


class SaleCreate(SaleBase):
    sale_items = Optional[List[SaleItemCreate]]


class SaleRead(SaleBase):
    id: int