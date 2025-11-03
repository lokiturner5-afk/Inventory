from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.stockmovementschema import StockMovementCreate, StockMovementRead
import models
from CRUD.stockmovement import stock_movement_crud
from database import get_db

routes = APIRouter(prefix="/stock-movement", tags=['Stock Movement/ Transactions'])


@routes.get("/get-movement-of-stocks", response_model=StockMovementRead)
def get_stock_movement(db:Session =Depends(get_db)):
    return stock_movement_crud.get_all(db)

@routes.post("/create_transaction", response_model=StockMovementRead)
def create_transaction(transaction:StockMovementCreate, db:Session = Depends(get_db)):
    return stock_movement_crud.create(db, transaction)

@routes.patch("/update-transaction/{transaction_id}", response_model=StockMovementRead)
def update_transaction(transaction:StockMovementCreate, db:Session = Depends(get_db)):
    return stock_movement_crud.update(db, transaction)

@routes.delete("/delete_item/{transaction_id}")
def remove_transaction(transaction_id:int, db:Session = Depends(get_db)):
    return stock_movement_crud.delete(db, transaction_id)