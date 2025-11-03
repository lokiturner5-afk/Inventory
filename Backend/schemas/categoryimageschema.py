from schemas.BaseSchema import BaseSchema
from pydantic import BaseModel
from typing import Optional


class CategoryImageBase(BaseModel):
    category_id: int
    image_url: str
    description: Optional[str] = None
    is_main: bool = False


class CategoryImageCreate(CategoryImageBase):
    pass


class CategoryImageRead(CategoryImageBase, BaseSchema):
    id: int