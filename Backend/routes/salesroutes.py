from fastapi import APIRouter, Depends
from schemas.saleschema import SaleRead, SaleCreate
from CRUD.salecrud import sale_crud
from sqlalchemy.orm import Session
from database import get_db
from typing import List


routes = APIRouter(prefix="/sales", tags=['Sales'])

@routes.get("/get-sales", response_model=List[SaleRead])
def get_sales(db:Session = Depends(get_db)):
    return sale_crud.get_all(db)

@routes.post("/create-sale", response_model=SaleRead)
def create_sale(sale:SaleCreate, db:Session = Depends(get_db)):
    return sale_crud.create_sale(db, sale)

@routes.patch("/update-sale/{sale_id}", response_model=SaleRead)
def update_sale(sale: SaleCreate, db:Session = Depends(get_db)):
    return sale_crud.update(db, sale)

@routes.delete("/delete_item/{sale_id}")
def delete_sale(sale_id:int, db:Session=Depends(get_db)):
    return sale_crud.delete(db, sale_id)

@routes.get('/sales-summary')
def get_sales_summary(db:Session = Depends(get_db)):
    return sale_crud.get_sales_summary(db)

@routes.get('/recent-sales')
def read_recent_sales(limit:int = 10, db:Session = Depends(get_db)):
    return sale_crud.get_recent_sales(limit=limit, db=db)