from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.warehouseschema import WarehouseCreate, WarehouseRead
import models
from CRUD.warehouse import warehouse_crud
from database import get_db
from typing import List
routes = APIRouter(prefix="/warehouse", tags=['Warehouse'])


@routes.get("/warehouse-info", response_model=List[WarehouseRead])
def warehouse_info(db:Session =Depends(get_db)):
    return warehouse_crud.get_all(db)

@routes.post("/create_warehouse_info", response_model=WarehouseRead)
def create_warehouse_info(transaction:WarehouseCreate, db:Session = Depends(get_db)):
    return warehouse_crud.create(db, transaction)

@routes.patch("/update-warehouse_info/{warehouse_id}", response_model=WarehouseRead)
def update_warehouse_info(warehouse:WarehouseCreate, db:Session = Depends(get_db)):
    return warehouse_crud.update(db, warehouse)

@routes.delete("/delete_item/{warehouse_id}")
def remove_warehouse_info(warehouse_id:int, db:Session = Depends(get_db)):
    return warehouse_crud.delete(db, warehouse_id)