# instance attributes are preffered more than class while assignment and retrival 
class employee: 
    
    language = "py"
    salary = 12000000
   
Yashi = employee() 
Yashi.language = "Yashi"
print(Yashi.language, Yashi.salary) # here language = Yashi and not py 