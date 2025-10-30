
from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from schemas.itemImageschema import ItemImageCreate
from datetime import datetime
from schemas.BaseSchema import BaseSchema



class ItemBase(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None
    unit_price: Decimal
    quantity: int = 0
    reorder_level: int = 10
    status: str = "active"


class ItemCreate(ItemBase):
    images: Optional[List[ItemImageCreate]] = None


class ItemRead(ItemBase, BaseSchema):
    id: Optional[int] = None
    images: Optional[List[ItemImageCreate]] = None
