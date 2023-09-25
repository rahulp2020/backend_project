
from sqlalchemy.orm import Session
from models.order import Order
from schemas.order.order import Createorder

def addorder(db: Session, user_data: Createorder):
    db_user = Order(**user_data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
