from CRUD.crud import CRUDBase
from schemas.stockmovementschema import StockMovementCreate
import models
from sqlalchemy.orm import Session

class CRUDStockMovement(CRUDBase[models.StockMovement, StockMovementCreate]):
    def record_movement(self, db:Session, obj_in:StockMovementCreate):
        movement = models.StockMovement(**obj_in.model_dump())
        db.add(movement)
        db.commit()
        db.refresh(movement)
        return movement
    
stock_movement_crud = CRUDStockMovement(models.StockMovement)