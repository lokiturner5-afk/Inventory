from fastapi import APIRouter, Depends
from database import get_db
from CRUD import usercrud
from sqlalchemy.orm import Session


routes = APIRouter(prefix="/me", tags=["Users"])



@routes.get("/get-users", status_code=200)
def get_users(db:Session = Depends(get_db)):
    return usercrud.get_users( db)