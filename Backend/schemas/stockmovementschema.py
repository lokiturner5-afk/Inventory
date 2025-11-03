from schemas.BaseSchema import BaseSchema
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class StockMovementBase(BaseModel):
    item_id: int
    warehouse_id: int
    movement_type: str
    quantity: int
    reference: Optional[str] = None


class StockMovementCreate(StockMovementBase):
    pass


class StockMovementRead(StockMovementBase, BaseSchema):
    id: int