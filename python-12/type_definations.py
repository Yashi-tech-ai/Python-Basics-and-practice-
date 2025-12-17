from typing import list , tuple , dict , union 
numbers: list[int] = [1,2,3,4]
string: tuple[str,int] = ("yashi", 19)
dictionnary: dict[int,str] = {1 : "yashi"}
unions: union[int,str] = "Id123" # means that anything from integer or string can come 
n : int = 5
name : str = "yashi"

def sum(a :int , b: int) -> int: # shows that integer will be returned
    return a+b

sum(2,3)