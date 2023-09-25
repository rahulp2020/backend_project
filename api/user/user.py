
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user.user import UserCreate,User
from services.user.user import create_user
from services.connection.db import get_db
from schemas.order.order import Createorder,Order
from services.order.order import addorder




router = APIRouter()

@router.post("/users/", response_model=User)
def sing_up(user_data: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user_data)
    return db_user

@router.post("/orderfinancials/", response_model=Order)
def purchage(user_data: Createorder, db: Session = Depends(get_db)):
    db_user = addorder(db, user_data)
    return db_user
