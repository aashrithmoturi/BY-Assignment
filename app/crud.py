from app.schemas import ProductCreate, ProductUpdate
from app import models
from sqlalchemy.orm import Session

def get_all_products(db: Session):
    return db.query(models.Product).all()

def get_product_by_id(id: int, db: Session):
    return db.query(models.Product).filter(models.Product.id == id).first()

def create_product(product: ProductCreate, db: Session):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update_product(id: int, update_data: ProductUpdate, db: Session):
    org_product = get_product_by_id(id, db)
    if org_product:
        update_dict = update_data.dict(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(org_product, key, value)

        db.commit()
        db.refresh(org_product)
    return org_product

def delete_product(id: int, db: Session):
    product = get_product_by_id(id, db)
    if product:
        db.delete(product)
        db.commit()
    return product