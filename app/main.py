from fastapi import FastAPI
from app.routers import products
from app.db import Base, engine
# from app.models import Product

# Create tables on startup
# TODO need to experiment with this
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(products.router)


# using hardcoded data of products
# products = [
#     Product(id=1, name="pen", price=5, quantity=100),
#     Product(id=2, name="pencil", price=4, quantity=200)
# ]
# @app.get("/products")
# def get_all_products():
#     return products

# @app.get("/product/{id}")
# def get_product_by_id(id: int):
#     for product in products:
#         if product.id == id:
#             return product
        
#     return {}

# @app.post("/product")
# def add_product(product: Product):
#     products.append(product)
#     return product

# @app.put("/product/{id}")
# def update_product(id: int, product: Product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return product
#     return {}

# @app.delete("/product/{id}")
# def delete_product(id: int):
#     for i in range(len(products)):
#         product = products[i]
#         if product.id == id:
#             products.pop(i)
#             return product
#     return {}