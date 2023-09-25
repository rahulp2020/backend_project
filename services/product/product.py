
from sqlalchemy.orm import Session
from models.product import product
from schemas.product.product import ProductCreate

def addproduct(db: Session, product_data: ProductCreate):
    db_user = product(**product_data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
