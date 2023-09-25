# models/user.py
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mobile = Column(String, unique=True, index=True)
    role = Column(String)
    orders = relationship('Order', back_populates='users')
    advisor_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    
    # Define a relationship for clients
    clients = relationship('User',foreign_keys=[advisor_id], back_populates='advisor')

    # Define a back-reference to the advisor
    advisor = relationship('User',remote_side=[id], back_populates='clients')
