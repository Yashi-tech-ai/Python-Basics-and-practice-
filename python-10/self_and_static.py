class employee: 
    language = "py"
    salary = 12000000
    
    def get_info(self):
        print(f"The language is {self.language} and salary is {self.salary}") 
    @staticmethod # default so  no need of self here 
    def greet():
         print("good morning pineapple ")
        
Yashi = employee() 
print(Yashi.language, Yashi.salary)
Yashi.get_info() # or you can write employee.get_info(Yashi)
employee.greet()

# def get_info() = if i had written in this way fir last mein jab call out krungi 
# print(f"The language is {language} and salary is {salary}") 
# is method se output  mein error aayega and it will say that 
# employee.get_info(Yashi) takes 0 positional arguments but 1 was given 