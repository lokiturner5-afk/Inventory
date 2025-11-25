from schemas.BaseSchema import BaseSchema
from typing import Optional, List
from decimal import Decimal
from schemas.saleitemBase import SaleItemCreate
from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    customer_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    sale_type: Optional[str] = None
    total_amount: Decimal = 0
    status: str = "completed"
    reference: Optional[str] = None


class SaleCreate(SaleBase):
    sale_items : Optional[List[SaleItemCreate]] = None
    


class SaleRead(SaleBase, BaseSchema):
    id: int
    sale_date:datetime
    