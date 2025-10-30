from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field, EmailStr, model_validator


# ==========================================================
# Base Schema
# ==========================================================
class BaseSchema(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# User Schemas
# ==========================================================
class UserBase(BaseSchema):
    username: str
    email: EmailStr
    role: Optional[str] = "staff"
    profile_image: Optional[str] = None


class UserCreate(BaseModel):
    
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: Optional[str] = "staff"
    profile_image: Optional[str] = None

class UserLogin(BaseModel):
    email:EmailStr
    password:str = Field(..., min_length=6)

    # model_config = ConfigDict(from_attributes=True)

class Tokenbase(BaseModel):
    access_token:str
    header: str
    model_config = ConfigDict(from_attributes=True)


class UserResponse(UserBase):
    pass


