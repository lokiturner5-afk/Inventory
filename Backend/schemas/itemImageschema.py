
from schemas.BaseSchema import BaseSchema
from pydantic import BaseModel
from typing import Optional

class ItemImageBase(BaseModel):
    item_id: int
    image_url: str
    description: Optional[str] = None
    is_main: bool = False


class ItemImageCreate(ItemImageBase):
    pass


class ItemImageRead(ItemImageBase, BaseSchema):
    id: int