
from pydantic import BaseModel

class Orderbase(BaseModel):
    user_id: int
    product_id: int

class Createorder(Orderbase):
    pass

class Order(Createorder):
    id: int

    class Config:
        orm_mode = True
