from fastapi import APIRouter, Depends
from database import get_db
import schema
from CRUD import usercrud
from sqlalchemy.orm import Session


routes = APIRouter(prefix="/me", tags=["Authentication"])



@routes.post("/signup", status_code=201)
def signup(user:schema.UserCreate, db:Session = Depends(get_db)):
    return usercrud.signup(user, db)

@routes.post("/login", status_code=201, )
def login(user:schema.UserLogin, db:Session = Depends(get_db)):
    return usercrud.login(user, db)