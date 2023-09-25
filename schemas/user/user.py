
from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    name: str
    mobile: str

class UserCreate(UserBase):
    role: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class createclient(UserCreate):
    advisor_id: int

class client(createclient):
    id: int

    class Config:
        orm_mode = True


class clientList(BaseModel):
    users: List[createclient]







