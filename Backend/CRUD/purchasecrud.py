from sqlalchemy.orm import Session
import models
from schemas.purchaseschema import PurchaseCreate
from schemas.purchaseItemschema import PurchaseItemCreate
from CRUD.crud import CRUDBase

class CRUDPurchase(CRUDBase[models.Purchase, PurchaseCreate]):
    def create_purchase(self, db:Session, obj_in:PurchaseCreate):
        purchase = models.Purchase(
            supplier_id=obj_in.supplier_id,
            warehouse_id=obj_in.warehouse_id,
            total_amount=obj_in.total_amount,
            status=obj_in.status,
            reference=obj_in.reference,
        )
        db.add(purchase)
        db.commit()
        db.refresh(purchase)

        if obj_in.purchase_items:
            for item in obj_in.purchase_items:
                db_item = models,PurchaseItemCreate(
                    item_id= item.item_id,
                    quantity= item.quantity,
                    unit_cost=item.unit_cost,
                    purchase_id=item.purchase.id,
                )
                db.add(db_item)
            db.commit()
        return purchase
    
purchase_crud = CRUDPurchase(models.Purchase)