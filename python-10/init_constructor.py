class employee: 
    language = "py"
    salary = 12000000

    def __init__(self,name,salary,language): # dunder method and it can self call themselves 
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object ")
    
    # def get_info(self): # self here point to yashi object downwards 
    #     print(f"The language is {self.language} and salary is {self.salary}") # so this is also an instance attribute 
    # @staticmethod 
    # def greet():
    #      print("good morning pineapple ")
        
Yashi = employee("anay", 13000000, "Javascript") 
# Yashi.name = "yashi" i want to make this easier more 
print(Yashi.language, Yashi.salary)
# Yashi.get_info() # or you can write employee.get_info(Yashi)
# employee.greet()
