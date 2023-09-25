
from sqlalchemy.orm import Session
from models.user import User
from schemas.user.user import UserCreate,createclient

def create_user(db: Session, user_data: UserCreate):
    db_user = User(**user_data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_client(db: Session, user_data: createclient):
    db_user = User(**user_data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def clients_list(db: Session, advisor_id: int):
    db_user=db.query(User).filter(User.advisor_id == advisor_id).all()
    # db_user=User(**db_user.dict())
    return db_user

