from fastapi import APIRouter, Depends
from schemas.categoryschema import CategoryRead, CategoryCreate
from CRUD.category import category_crud
from sqlalchemy.orm import Session
from database import get_db


routes = APIRouter(prefix="/categories", tags=['Categories'])

@routes.get("/get-categories", response_model=CategoryRead)
def get_categories(db:Session = Depends(get_db)):
    return category_crud.get_all(db, 100)


@routes.post("/add-category", response_model=CategoryRead)
def add_category(category:CategoryCreate, db:Session = Depends(get_db)):
    return category_crud.create_category(db, category)

@routes.patch("/update-category/{category_id}", response_model=CategoryRead)
def update_category(category:CategoryCreate, db:Session= Depends(get_db)):
    return category_crud.update(db, category)

@routes.delete("/delete-category/{category_id}")
def delete_category(category_id:int, db:Session =Depends(get_db)):
    return category_crud.delete(db, id)