# models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

class product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    category = Column(String,unique=True)
    orders = relationship('Order', back_populates='products')
