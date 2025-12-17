class student:
    name = "Yashi"
    def __init__(self,fullname):
       self.name = fullname
       print(f"Hello {self.name}")
    # def __init__(self): # default constructors
    #     pass
    def welcome(self): # methods 
        print(f"Hello here users! {self.name}")
anay = student("sarita")
# anay.name = "Sarita"
print(anay.name)
anay.welcome()