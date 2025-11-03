from fastapi import APIRouter, Depends
from database import get_db
from schemas.purchaseschema import PurchaseCreate, PurchaseRead
from CRUD.purchasecrud import purchase_crud
from sqlalchemy.orm import Session


routes = APIRouter(prefix="/purchases", tags=['Purchases'])

@routes.get("/get-purchase", response_model=PurchaseRead)
def get_purchsaes(db:Session = Depends(get_db)):
    return purchase_crud.get_all(db, 100)

@routes.post("/create_purchase_slip", response_model=PurchaseRead)
def create_purcahse_slip(purchase:PurchaseCreate, db:Session = Depends(get_db)):
   return purchase_crud.create_purchase(db, purchase)

@routes.patch("/update-purhcase-slip/{purchase_id}", response_model=PurchaseRead)
def update_purchase_slip(purchase:PurchaseCreate, db:Session = Depends(get_db)):
    return purchase_crud.update(db, purchase)


@routes.delete("/delete-item/{purchase_id}")
def remove_item(purchase_id:int, db:Session = Depends(get_db)):
    return purchase_crud.delete(db, purchase_id)