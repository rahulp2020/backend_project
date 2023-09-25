from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.product.product import Product,ProductCreate
from services.product.product import addproduct
from services.connection.db import get_db

router = APIRouter()

@router.post("/addproduct/", response_model=Product)
def createproduct(user_data: ProductCreate, db: Session = Depends(get_db)):
    db_user = addproduct(db, user_data)
    return db_user
