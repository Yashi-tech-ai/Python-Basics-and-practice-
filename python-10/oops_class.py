# object oriented programming = solving a problem by creating object is one of the most popular approaches in programming 
# focuses on resuseable code = dry principle 
# CLASS =>
# blueprint of creating an object i.e contains info to be filled in to  make an object 
class employee: # noun 
     # attributes = language and salary jo hai vo attributes hai 
    language = "py"
    salary = 12000000
    # now to make an object =>
Yashi = employee() # verb 
Yashi.name = "Yashi"
print(Yashi.language, Yashi.salary)

anay = employee()
anay.name = "Anay"
print(anay.name,anay.salary , anay.language)

# class attributes = an attribute which belongs to a class rather than an object 
#instance attribute = an attribute which belongs to a object rather than a class
# yahan pe language and salary class attributes hai and name instance attribute hai 