from fastapi import APIRouter,Depends
from schemas.user.user import createclient, client,clientList
from services.connection.db import get_db
from sqlalchemy.orm import Session
from services.user.user import create_client,clients_list
router = APIRouter()

@router.post("/add_client/", response_model=client)
def add_client(user_data: createclient, db: Session = Depends(get_db)):
    db_user = create_client(db, user_data)
    return db_user

@router.get("/clientslist/{advisor_id}")
def get_clients(advisor_id: int, db: Session = Depends(get_db)):
    db_user = clients_list(db, advisor_id)
    return db_user

    


