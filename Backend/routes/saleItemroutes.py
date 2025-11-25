from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from schemas.saleitemBase import SaleItemCreate, SaleItemRead
import models
from CRUD.salesItems import saleItem_crud
from typing import List

routes = APIRouter(prefix='/sales-items', tags=['Sale Items'])

@routes.get('/all-sale-items', response_model=List[SaleItemRead])
def get_sale_items(db:Session = Depends(get_db)):
    return saleItem_crud.get_all(db)

@routes.get('/get-sale-item/{item_id}', response_model=SaleItemRead)
def get_sale_item(item_id:int, db:Session = Depends(get_db)):
    return saleItem_crud.get(item_id, db)

@routes.post('/add-sale-item', response_model=SaleItemRead)
def add_sale_item(saleItem:SaleItemCreate, db:Session = Depends(get_db)):
    return saleItem_crud.create(db, saleItem)

@routes.patch('/update-sale-item/{item_id}')
def update_item(saleItem:SaleItemCreate, db:Session = Depends(get_db)):
    return saleItem_crud.update(db, saleItem)

@routes.delete('/delete-sale-item/{item_id}')
def delete_sale_item(item_id:int, db:Session = Depends(get_db)):
    return saleItem_crud.delete(db, item_id)