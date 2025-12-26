from fastapi import  Depends, FastAPI
from models import product
from database import session,engine
import database_models
from sqlalchemy.orm import Session


app=FastAPI()

database_models.base.metadata.create_all(bind=engine)




@app.get("/")
def greet():
    return("welcome to mydomain")

products=[
  product  (id=1,name="phone",description="big phone",price=200,quantity=10),
  product (id=2,name="mobile",description="big mobiles",price=300,quantity=11),
  product (id=3,name="computer",description="big mobilse",price=400,quantity=12),
  product (id=4,name="laptop",description="big mobisle",price=500,quantity=13),
  product (id=5,name="notepad",description="big msobile",price=600,quantity=14),]

def get_db():
   db=session()
   try:
       yield db
   finally:     
      db.close()

def init_db():
   db=session()

   count = db.query(database_models.product).count
   if count==0:
    for product in products:
      db.add(database_models.product(**product.model_dump()))

      db.commit()

            
          
          



init_db()

@app.get("/products")
def get_all_products(db:Session=Depends(get_db)):
   db_Products=db.query(database_models.product).all()
   return db_Products

@app.get("/product/{id}")
def  get_product_by_id (id:int):
    for product in products:
      if product.id==id:
       return product
    
       
       return "product not found"
      

@app.post("/product")
def add_product(product:product):
   products.append(product)
   return product
   
@app.put("/product")
def update_product(id:int,product:product):
   for i in range(len(products)):
      if products[i].id==id:
          products[i]=product
          return "product added succesfully"
          
          return "no product found "
    
@app.delete("/product") 
def delete_product(id:int):
   for i in range(len(products)):
      if products[i].id==id:
         del products[i]  
         return "product is deleted "
         return "product not found "               
         



