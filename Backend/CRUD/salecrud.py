from sqlalchemy.orm import Session
from CRUD.crud import CRUDBase
from schemas.saleschema import SaleCreate
from schemas.saleitemBase import SaleItemCreate
from sqlalchemy import func
import models

class CRUDSale(CRUDBase[models.Sale, SaleCreate]):
    def create_sale(self, db:Session, obj_in:SaleCreate):
        sale = models.Sale(
            customer_id = obj_in.customer_id,
            warehouse_id=obj_in.warehouse_id,
            sale_date=obj_in.sale_type,
            total_amount=obj_in.total_amount,
            status=obj_in.status,
            reference=obj_in.reference,
        )
        db.add(sale)
        db.commit()
        db.refresh(sale)

        if obj_in.sale_items:
            for item in obj_in.sale_items:
                db_item = SaleItemCreate(
                    item_id=item.item_id,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                    sale_id=sale.id,
                )
                db.add(db_item)
            db.commit()
        return sale
    
    def get_sales_summary(self, db:Session):
        results = (
            db.query(
                func.date( models.Sale.sale_date).label('date'),
                func.sum(models.Sale.total_amount).label('total_sales')
            )
            .group_by(func.date( models.Sale.sale_date))
            .order_by(func.date( models.Sale.sale_date))
            .all()
        )
        return [{"date": str(r.date), "total_sales": float(r.total_sales)} for r in results]
    

sale_crud = CRUDSale(models.Sale)