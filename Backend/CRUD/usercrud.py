from sqlalchemy.orm import Session
import models, schema
from fastapi import HTTPException
from passlib.context import CryptContext
import auth


pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')


def get_user( db:Session, user_id:int=None, user_email:str=None):
    if user_id:
        return db.query(models.User).filter(models.User.id == user_id).first()
    if user_email:
        return db.query(models.User).filter(models.User.email == user_email).first()
    

def get_users(db:Session):
    return  db.query(models.User).all()

def get_username(email:str):
    return email.split("@")[0]
    
def hashed_password(password:str):
    if len(password) >= 8:
        return pwd_context.hash(password)
    else:
        raise HTTPException(status_code=401, detail="Password has less charcters, 8 or more")
    
def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def signup(user:schema.UserCreate, db:Session):
    existing_user = get_user(db, user_email=user.email)
    if existing_user:
        raise HTTPException(detail="REJECTED!", status_code=401)
    data = models.User(
        username= get_username(user.email),
        email=user.email,
        password=hashed_password(user.password),
        role=user.role
    )
    db.add(data)
    db.commit()
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "headers":"Bearer"}


    
def login(user:schema.UserLogin, db:Session):
    existing_user = get_user(db, user_email=user.email)
    if not existing_user:
        raise HTTPException(detail="Invalid Password or Email")
    
    if not verify_password(user.password, existing_user.password):
        raise HTTPException(detail="Invalid Password or Email")
    
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "headers": "Bearer"}
    