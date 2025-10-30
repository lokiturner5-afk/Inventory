from sqlalchemy.orm import Session
import models
from schemas.itemschema import ItemCreate
from CRUD.crud import CRUDBase
from datetime import datetime
import random
import string

class CRUDItem(CRUDBase[models.Item, ItemCreate]):

    def _generate_sku(self, db: Session, name: str) -> str:
        """Generate a unique SKU based on item name and current date."""
        # Create base part: e.g. "ITEM" or first 3 letters of the name
        prefix = (name[:3].upper() if name else "ITM")

        # Add date and random letters: e.g. "20251029-AB12"
        date_part = datetime.utcnow().strftime("%Y%m%d")
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        sku = f"{prefix}-{date_part}-{random_part}"

        # Ensure SKU uniqueness in the database
        while db.query(models.Item).filter(models.Item.sku == sku).first():
            random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            sku = f"{prefix}-{date_part}-{random_part}"

        return sku


    def create_item(self, db: Session, obj_in: ItemCreate):
        # Auto-generate SKU if not provided
        sku = obj_in.sku or self._generate_sku(db, obj_in.name)

        item = models.Item(
            name=obj_in.name,
            sku=sku,
            description=obj_in.description,
            category_id=obj_in.category_id,
            supplier_id=obj_in.supplier_id,
            unit_price=obj_in.unit_price,
            quantity=obj_in.quantity,
            reorder_level=obj_in.reorder_level,
            status=obj_in.status,
        )
        db.add(item)
        db.commit()
        db.refresh(item)

        # Handle images if any
        if obj_in.images:
            for img in obj_in.images:
                db_image = models.ItemImage(
                    image_url=img.image_url,
                    description=img.description,
                    is_main=img.is_main,
                    item_id=item.id,
                )
                db.add(db_image)
            db.commit()

        return item


item_crud = CRUDItem(models.Item)
