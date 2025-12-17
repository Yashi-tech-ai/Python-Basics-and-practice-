class employee: 
    def show(self):
        self.name = "default name"
        self.compnay = "porsche"
        print(f"The name is {self.name} and salary is {self.company}")

class coder:
    language = "python"
    def printlanguages(self):
        print(f"out of all the languages here is your language = {self.language }")

class programmer(employee, coder): 
    company = "Maybach"
    def showlanguage(self):
        print(f"The name is {self.company} and is good in {self.language}")


a = employee()
b = programmer()
b.show()
b.showlanguage()
b.printlanguages()