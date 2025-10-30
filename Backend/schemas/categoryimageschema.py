from schemas.BaseSchema import BaseSchema
from typing import Optional


class CategoryImageBase(BaseSchema):
    category_id: int
    image_url: str
    description: Optional[str] = None
    is_main: bool = False


class CategoryImageCreate(CategoryImageBase):
    pass


class CategoryImageRead(CategoryImageBase):
    id: int