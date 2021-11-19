# Python
from typing import Optional, List

# FastAPI (Pydantic)
from pydantic import BaseModel, EmailStr, Field

class ItemBase(BaseModel):
  title: str
  description: Optional[str] = None

class ItemCreate(ItemBase):
  pass

class Item(ItemBase):
  id: int = Field(...)
  owner_id: int = Field(...)
  class Config():
    orm_mode = True

class UserBase(BaseModel):
  email: EmailStr = Field(...)

class UserCreate(UserBase):
  password: str = Field(..., min_length=8, max_length=25)

class User(UserBase):
  id: int = Field(...)
  is_active: bool = Field(...)
  items: List[Item] = []
  class Config:
    orm_mode = True