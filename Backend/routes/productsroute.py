from fastapi import APIRouter, Depends
from CRUD.product import  item_crud
from schemas.itemschema import ItemRead, ItemCreate
from database import get_db
from sqlalchemy.orm import Session
import models


routes = APIRouter(prefix="/products", tags=["Products"])


@routes.get("/")
def get_products(db:Session = Depends(get_db)):
    return item_crud.get_all(db)

@routes.post("/add-product", response_model=ItemRead)
def add_product(item:ItemCreate, db:Session=Depends(get_db)):
    return item_crud.create_item(db, item)

@routes.patch("/update-item/{item_id}", response_model=ItemRead)
def update_product(item_id:int, item:ItemCreate, db:Session=Depends(get_db)):
    return item_crud.update(db, models.Item,  item)

@routes.delete("/delete-item/{item_id}")
def delete_item(item_id:int, db:Session = Depends(get_db)):
    return item_crud.delete(id=item_id, db=db)