from typing import  Optional, List
from schemas.BaseSchema import BaseSchema
from categoryimageschema import CategoryImageCreate

class CategoryBase(BaseSchema):
    style: str
    category_type: str
    material: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    images: Optional[List[CategoryImageCreate]] = None

class CategoryRead(CategoryBase):
    id:int