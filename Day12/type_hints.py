from typing import Optional

name:str = "Ayush"
age:int = 21
price:float = 49.99
is_number:bool = True
tag:list[str] = ["Ai","Python"]
scores:dict[str,int]={"Math":92,"science":13}
nickname:Optional[str]=None

print(name)
print(age) 

def  total_price(price:floatm,qty:int) -> float:
    return price*qty