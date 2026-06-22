#pip install pydentic

from pydantic import BaseModel, Field, ValidationError

class Product(BaseModel):
    name:str
    price:float = Field(gt=0)  #greater then 0
    tags:list[str]=[]

pen = Product(name="Gelpen",price=10,tags=["pems","pencils"])
print(pen)

#item = product(name"Broken",price=-5)
# print(item)

try:
    Product(name="Broken",price=-5)
except ValidationError as err:
    print("caught validation error")
    print(err.errors()[0]["msg"])