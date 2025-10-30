from sqlalchemy.orm import Session
from database import get_db
from CRUD.suppliercrud import supplier_crud
from schemas.supplierschema import SupplierRead, SupplierCreate
from fastapi import APIRouter, Depends


routes = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@routes.get("/get-supplier", response_model=SupplierRead)
def get_supplier(db:Session=Depends(get_db)):
    return supplier_crud.get_all(db)

@routes.post("/add-supplier", response_model=SupplierRead)
def add_supplier(supplier:SupplierCreate, db:Session=Depends(get_db)):
    return supplier_crud.create(db, supplier)

