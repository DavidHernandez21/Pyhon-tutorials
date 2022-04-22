from fastapi import FastAPI
from dotenv import load_dotenv
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from os import getenv
import pathlib

load_dotenv(pathlib.Path(pathlib.Path(__file__).parent.parent.absolute(), ".env"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    # allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host=getenv("REDIS_HOST"),
    port=getenv("REDIS_PORT"),
    password=getenv("REDIS_PASSWORD"),
    decode_responses=True,
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

def get_product(product_pk: str):
    product = Product.get(product_pk)

    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
    }

@app.get("/products")
async def get_products():
    # print(dir(Product))
    return [get_product(product_pk) for product_pk in Product.all_pks()]


@app.post("/products")
async def create_product(product: Product):
    return product.save()

@app.delete("/products/{product_pk}")
async def delete_product(product_pk: str):
    return Product.delete(product_pk)

@app.get("/products/{product_pk}")
async def get_product_by_id(product_pk: str):
    return Product.get(product_pk)
    

