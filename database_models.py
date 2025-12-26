from sqlalchemy import Column,String,Integer,Float
from sqlalchemy.ext.declarative import declarative_base



base=declarative_base()

class product(base) :

    __tablename__ ="product"


    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)
    quantity=Column(Integer)
