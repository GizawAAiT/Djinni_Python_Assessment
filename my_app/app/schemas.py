from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr

class PostCreate(BaseModel):
    text: str

class PostResponse(BaseModel):
    id: int
    text: str
