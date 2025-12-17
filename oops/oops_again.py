# class student:
#     name = "Yashi"
#     def __init__(self,fullname):
#        self.name = fullname
#        print(f"Hello {self.name}")
#     # def __init__(self): # default constructors
#     #     pass
#     def welcome(self): # methods 
#         print(f"Hello here users! {self.name}")
# anay = student("sarita")
# # anay.name = "Sarita"
# print(anay.name)
# anay.welcome()

# class student:

#     def __init__(self,subject,marks):
#         self.subject = subject
#         self.marks = marks
#     def average(self):
#         sum = 0
#         for value in self.marks:
#             sum += value
#         print("Hello your average score is: ", sum/3 )
#     @staticmethod # decorator
#     def hello():
#         print("Hello")

# yashi = student("Maths",[95,98,95])
# yashi.average()
# yashi.hello()


# abstraction method 
# class car:
#     def __init__(self):
#         self.accelerator = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.accelerator = True
#         self.clutch = True
#         print("Car started ....")

# car1 = car()
# car1.start()


# capsule method = data + function in a single unit 

# class account:
#     balance = 54000000000
#     account_no = 1234
    
#     @staticmethod
#     def show_balance():
#         print("Your balance is : " ,account.balance)
#     @staticmethod
#     def show_account_no():
#         print("Your account number  is : " ,account.account_no)

#     def debit(self,amount):
#         self.balance = self.balance - amount
#         print("$ " , amount , "was debited from your account")
#         print("Total balance = ", self.balance)
#     def credit(self,amount):
#         self.balance = self.balance + amount
#         print("$ " , amount , "was credited from your account")
#         print("Total balance = ", self.balance)
#     def get_balance(self):
#         return self.balance

# user = account()
# user.show_balance()
# user.show_account_no()
# user.debit(45000)
# user.credit(32323232)



# deleting an object 
# class student:
#     def __init__(self,name):
#         self.name = name
    
# yashi = student("Yashi")
# del yashi.name
# print(yashi.name)


# public and private attributes 
# public can be accesed outside class 
# class account:
#     __name = "Yashi" # this is a private att.
#     # def __init__(self,balance, account_no):
#     #      self.balance = balance
#     #      self.__account_no = account_no # __account_no is private attribute but if we make a function in class which print
#         #  the account number and then call it in object than it will show 
#     def __hello(self): # this is  a private method 
#          print("Hello user!")
#     def welcome(self): # but this can call and print the hello function 
#          self.__hello()

# user = account()  #public attribute 
# # print(user.balance)
# # print(user.__account_no)
# print(user.welcome())
 

# COMPOSITION = Composition means one class contains objects of other classes as attributes.
# class salary:
#     def __init__(self,pay,bonus):
#         self.pay = pay
#         self.bonus = bonus
    
#     def annual_salary(self):
#         return (self.pay*12) + (self.bonus)

# class employee:
#     def __init__(self,name,pay,bonus):
#         self.name = name
#         self.obj_salary = salary(pay,bonus)
#     def total_salary(self):
#         return self.obj_salary.annual_salary()

# emp = employee('Max', 40000, 500)
# print(emp.total_salary())


# AGGREGATION :
# class salary:
#     def __init__(self,pay,bonus):
#         self.pay = pay
#         self.bonus = bonus
    
#     def annual_salary(self):
#         return (self.pay*12) + (self.bonus)

# class employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.obj_salary = salary
#     def total_salary(self):
#         return self.obj_salary.annual_salary()


# salary =  salary(40000, 500)
# emp = employee('Max')


# INHERITANCE
# class car: # parent class 
#      @staticmethod
#      def start():
#           print("Car started...")
#      @staticmethod
#      def stop():
#           print("Car stopped ...")
# class ToyotaCar(car): # child class 
#      def __init__(self,name):
#           self.name = name 

# c1 = car()
# c2 = ToyotaCar("Porsche")
# print(c2.start())


# MULTILEVEL INHERITANCE 
# class car: # parent class 
#      @staticmethod
#      def start():
#           print("Car started...")
#      @staticmethod
#      def stop():
#           print("Car stopped ...")
# class ToyotaCar(car): # child class 
#      def __init__(self,brand):
#           self.brand = brand
# class fortuner(ToyotaCar):
#      def __init__(self, type):
#           self.type = type

# c1 = fortuner("Petrol")
# print(c1.stop())

    
# MULTIPLE INHERITANCE = multiple parent/ base class 
# class A:
#     varA = "Welcome to class A"
 
# class B:
#     varB = "Welcome to class B"

# class orientation(A,B):
#     print("Welcome to the new session")

# c1 = orientation()
# print(c1.varA)
# print(c1.varB)
# print(c1)


# Super = used to access methods of parent class 
# class car: 
#      def __init__(self,type):
#           self.type = type
#      @staticmethod
#      def start():
#           print("Car started...")
#      @staticmethod
#      def stop():
#           print("Car stopped ...")
# class ToyotaCar(car): 
#      def __init__(self,brand,type):
#           super().__init__(type)
#           self.brand = brand
#           super().start()

# car1 = ToyotaCar("Fortuner","Automatic")
# print(car1.type)


# Class method
# class person:
#     name = "Anonymus"
    
#     @classmethod
#     def changename(cls,name):
#           cls.name = name  # this won't chnage the name in the full class since this creates another one name 
#         #  so to change = 
#         # person.name = name # or 
#         # self.__class__.name = name # or by directly using class method on function

# p1 = person()
# p1.changename("Yashi Sharma")
# print(p1.name)
# print(person.name)


# property method 
# class students:
#      def __init__(self,maths,sci):
#           self.maths = maths 
#           self.sci= sci 

#      @property # latest values will be used here 
#      def changepercentage(self):
#         return str(self.maths + self.sci) 

# st1 = students(56,34)
# print(st1.changepercentage)

# st1.sci = 89
# print(st1.changepercentage )


# Polymorphism  : operator overloading 
class complex:
    def __init__(self,real,img):
        self.real = real 
        self.img = img

    def shownumber(self):
        print(self.real , "i + " ,self.img, "j")

    def __add__(self,num):
        newreal = self.real + num.real
        newimg = self.img + num.img
        return complex(newreal,newimg)

a = complex(2,3)
a.shownumber()

# b = complex(4,5)
# b.shownumber()

# total = a + b
# total.shownumber()