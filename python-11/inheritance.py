class employee: # base class / parent class  = yahan pe jo change aayega na vo neeche wali class mein bhi aayega 
    company = "porsche"
    def show(self,name,salary):
        self.name = name 
        self.salary = salary
        print(f"The name is {self.name} and salary is {self.salary}")

# class programmer:
#     company = "Maybach"
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is {self.name} and is good in {self.language}")

class programmer(employee): # inherit class / derived class = saare methods and attributes yahan aa jayenge upar change krte hi 
    company = "Maybach"
    def showlanguage(self):
        print(f"The name is {self.name} and is good in {self.language}")


a = employee()
b = programmer()
print(b.show("Yashi", 212121))
print(a.company,b.company)

