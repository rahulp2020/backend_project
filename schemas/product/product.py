from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    category: str

class ProductCreate(ProductBase):
    pass

class Product(ProductCreate):
    id: int

    class Config:
        orm_mode = True
