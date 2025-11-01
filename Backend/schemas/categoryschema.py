from typing import  Optional, List
from schemas.BaseSchema import BaseSchema
from schemas.categoryimageschema import CategoryImageCreate
from pydantic import BaseModel

class CategoryBase(BaseModel):
    style: str
    category_type: str
    material: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    images: Optional[List[CategoryImageCreate]] = None

class CategoryRead(CategoryBase, BaseSchema):
    id:int