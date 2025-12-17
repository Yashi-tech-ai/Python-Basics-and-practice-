# print("HELLO ")

# a = 1
# b = 5.6
# c = "hello"
# d = True or False
# e = a + b
# print(e)
# inp = int(input("Enter a number : "))
# print(inp)
# print(type(b))
# h = int(b)
# print(type(h))

# a = b = c = 1
# a, b, c = 23, 29.45," Ram"
# print(a,b,c)

# a = "Hello"
# print(a*4)

# x = [1, 2, 3]
# y = [4, 5]   
# print(x+y)

# l = [1,2,4,5.6,True,"Hello"]
# t= (1,2,4,5.6,True,"Hello")
# d = {'name': 'amit', 'age': 20, 'ID': 20}
# s =  {'a', 'e', 'i', 'o', 'u'}
# print(5>3)


# ternary operator 
# age = 17
# result = "Adult" if age >= 18 else "Minor"
# print(result)   


# msg = "Hello!"
# index = 0
# for i in msg:
#     print("msg[", index, "] =", i)
#     index += 1


# name = "Yashi"
# print("Name = %s",(name))

# print("Hi how are you ! \n I am good ")

# age = int(input("Enter your age :"))
# if(age >= 18):
#     print("Ogayy")
# elif(age <18):
#     print("Not ogayy")
# else:
#     print("Hi")


# l = [1,2,3,4,4]
# for i in l:
#     print(i)

# for i in range(0,20,3):
#     print(i)

# i = 0
# while(i < 4):
#     print(i)
#     i+= 1

# # comprehensions 
# mylist = [23 ,34,45,56,567]
# square = [i*i for i in mylist] # [expression for  i in list or whatever]
# print(square)

# enumerators = index along with the value in a loop.
# for index, i in enumerate(mylist):
#     print(index,",",i)


# (a, b, c)= (1, 2, 3)
# print (a, b, c)


# def square(n):
#  '''Takes in a number n, returns the square of n''' 
#  return n**2
# print(square.__doc__) 
# print(square(4))


# *args
# def greet(*names):
#     for name in names:
#         print("Hello", name)

# greet("Bambi", "Yashi", "Alex")


# **kwargs
# def introduce(**info):
#     for key, value in info.items():
#         print(key, ":", value)

# introduce(name="Bambi", age=19, course="CSE")


# a = dir(__builtins__)
# print(a)


# enclosing namespace 
# def outer():
#     x = "I belong to outer"

#     def inner():
#         print(x)   # inner uses outer's variable

#     inner()

# outer()


# filter 
# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # [2, 4, 6]


# map
# nums = [1, 2, 3, 4]
# squares = list(map(lambda x: x**2, nums))
# print(squares)  # [1, 4, 9, 16]


# reduce 
# from functools import reduce
# nums = [1, 2, 3, 4]
# total = reduce(lambda x, y: x + y, nums)
# print(total)  # 10


# generators 
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# gen = count_up_to(5)
# for num in gen:
#     print(num)   # 1 2 3 4 5


# decorators
# def mydecorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper

# @mydecorator
# def say_hello():
#     print("Hello!")

# say_hello()


# oops
class employee:
    atr1= "dog"
    atr2= " brown"

    def fun(self):
        print("dog is a ",self.atr1)
        print("dog is a ",self.atr2)
        
    def __init__(self,breed):
        self.breed = breed
        print(self.breed)
    
    @staticmethod
    def greet():
        print("good morninnngggg")

doggie = employee("retriver")
doggie.name = "HIIIII"
doggie.atr1 = "cutiee"
print(doggie.name)
print(doggie.atr1)
print(doggie.atr2)
doggie.fun()
doggie.greet()