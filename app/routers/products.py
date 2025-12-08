from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.schemas import Product, ProductCreate, ProductUpdate
from app.db import get_db
from app import crud

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=list[Product])
def get_all_products(db: Session = Depends(get_db)):
    try:
        products = crud.get_all_products(db)
        return products
    
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

@router.get("/{id}", response_model=Product)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    try:
        product = crud.get_product_by_id(id, db)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        return product

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        new_product = crud.create_product(product, db)
        return new_product
    
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

@router.put("/{id}", response_model=Product)
def update_product(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    try:
        updated_product = crud.update_product(id, product, db)
        if not updated_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        return updated_product

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

@router.delete("/{id}", response_model=Product)
def delete_product(id: int, db: Session = Depends(get_db)):
    try:
        deleted_product = crud.delete_product(id, db)
        if not deleted_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
        return deleted_product

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )
