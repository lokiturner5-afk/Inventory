from fastapi import APIRouter, Depends
from schemas.categoryschema import CategoryRead, CategoryCreate
from CRUD.category import category_crud
from sqlalchemy.orm import Session
from database import get_db


routes = APIRouter(prefix="/categories", tags=['Categories'])

@routes.post("/add-category", response_model=CategoryRead)
def add_category(category:CategoryCreate, db:Session = Depends(get_db)):
    return category_crud.create_category(db, category)