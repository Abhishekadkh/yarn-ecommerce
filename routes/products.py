from fastapi import APIRouter, HTTPException
from schemas.product import Product
from typing import List
from uuid import uuid4

router = APIRouter(prefix="/products", tags=["Products"])

products = []

@router.get("/", response_model=List[Product])
def get_all_products():
    return products

@router.post("/", response_model=Product)
def create_product(product: Product):
    product.id = str(uuid4())
    products.append(product)
    return product

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: str):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/{product_id}")
def delete_product(product_id: str):
    global products
    products = [p for p in products if p.id != product_id]
    return {"message": "Product deleted"}
