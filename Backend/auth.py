from fastapi import HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY= os.getenv('SECRET_KEY') 
ALGORITHM= os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_token(data:dict, expires_delta:timedelta|None=None):
    to_encode = data.copy()
    if  expires_delta:
        expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp": int(expire.timestamp()),
        "iat": int(datetime.now(timezone.utc).timestamp())
    })
    encoded = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded

def verify_token(token:str):
    try:
        return jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token or token has expired")