# models/order.py
from sqlalchemy import Column, Integer, String,ForeignKey,DateTime,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, default=func.now(), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id',ondelete="SET NULL"))
    product_id = Column(Integer, ForeignKey('products.id',ondelete="SET NULL"))
    users = relationship('User', back_populates='orders')
    products = relationship('product', back_populates='orders')

    
