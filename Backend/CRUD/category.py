from sqlalchemy.orm import Session
import models
from schemas.categoryschema import CategoryCreate
from crud import CRUDBase


class CRUDCategory(CRUDBase[models.Category, CategoryCreate]):
    def create_category(self, db:Session, obj_in:CategoryCreate):
        category = models.Category(
            style= obj_in.style,
            category_type=obj_in.category_type,
            material=obj_in.material,
            description=obj_in.description,
        )
        db.add(category)
        db.commit()
        db.refresh(category)


        if obj_in.images:
            for img in obj_in.images:
                db_image = models.CategoryImage(
                    image_url=img.image_url,
                    description=img.description,
                    is_main=img.is_main,
                    category_id=category.id,
                )
                db.add(db_image)
            db.commit()
        return category
    
category_crud =CRUDCategory(models.Category)