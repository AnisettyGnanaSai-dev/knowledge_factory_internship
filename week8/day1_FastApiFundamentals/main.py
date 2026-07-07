from fastapi import FastAPI, Depends
from models import Product
from database import SessionLocal,engine
import database_models
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods = ["*"]
)
database_models.Base.metadata.create_all(bind = engine)


@app.get("/")
def greet():
     return "Welcome to Telusko!"

products = [
    Product(
        id=1,
        name="Phone",
        description="iPhone",
        price=999,
        quantity=10
    ),
    Product(
        id=2,
        name="Laptop",
        description="Asus Laptop",
        price=1000,
        quantity=20
    )
]

def get_db():
     db = SessionLocal()
     try :
          yield db
     finally:
          db.close()

def init_db():
     db = SessionLocal()
     
     count = db.query(database_models.Product).count()
     if count == 0:
          for product in products:
               db.add(database_models.Product(**product.model_dump()))
          db.commit()


init_db()


@app.get("/products")
def get_all_products(db :Session = Depends(get_db)):
    #  db = SessionLocal()
    #  db.query()
    db_products = db.query(database_models.Product).all()

    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db :Session = Depends(get_db)):
    # for product in products:
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product == id:
        return db_product
    # return {"message": "Product not found!"}

@app.post("/products")
def add_product(product : Product, db :Session = Depends(get_db)):
    #  products.append(product)
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.delete("/products/{id}")
def delete_product_by_id(id : int,  db :Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
     db.delete(db_product)
     db.commit()
            #    del products[i]
            #    return "Product deleted"
     return {"message": "Product deleted !"}

@app.put("/products/{id}")
def update_product(id : int,product : Product, db :Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated!"
    else:
         
        # products[i] = product
        # return "Product added succesfully!"
        # 
        return "No product found"
