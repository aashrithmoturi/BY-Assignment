from pydantic import BaseModel

class ProductBase(BaseModel): 
    name: str
    price: float
    category: str

class ProductCreate(ProductBase):
    pass 

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    category: str | None = None

class Product(ProductBase):
    id: int

    # TODO try playing with this remove
    class Config:
        orm_mode = True