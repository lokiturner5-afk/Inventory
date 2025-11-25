from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.customerschema import CustomerRead, CustomerCreate
import models
from CRUD.customer import customer_crud
from typing import List

routes = APIRouter(prefix="/customer", tags=['Customer'])

@routes.get('/get-customers', response_model=List[CustomerRead])
def get_customers(db:Session=Depends(get_db)):
    return customer_crud.get_all(db)

@routes.get('/get-customer/{customer_id}', response_model=CustomerRead)
def get_customer(customer_id:int, db:Session=Depends(get_db)):
    return customer_crud.get(customer_id, db)

@routes.post('/add-customer', response_model=CustomerRead)
def add_customer(customer:CustomerCreate, db:Session = Depends(get_db)):
    return customer_crud.create(db, customer)

@routes.patch('/update-customer/{customer_id}')
def update_customer( customer:CustomerCreate, db:Session = Depends(get_db)):
    return customer_crud.update(db, customer)

@routes.delete('/delete-customer/{customer_id}')
def delete(customer_id:int, db:Session = Depends(get_db)):
    return customer_crud.delete(db, customer_id)