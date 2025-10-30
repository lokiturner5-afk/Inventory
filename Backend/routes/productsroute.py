from fastapi import APIRouter, Depends
from CRUD.product import  item_crud
from schemas.itemschema import ItemRead, ItemCreate
from database import get_db
from sqlalchemy.orm import Session


routes = APIRouter(prefix="/products", tags=["Products"])


@routes.get("/", response_model=ItemRead)
def get_products(db:Session = Depends(get_db)):
    item_crud.get_all(db)

@routes.post("/add-product", response_model=ItemRead)
def add_product(item:ItemCreate, db:Session=Depends(get_db)):
    item_crud.create(db, item)