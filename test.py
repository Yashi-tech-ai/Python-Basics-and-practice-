# def numbers():
#     for i in range(3):
#         yield i*5

# gen = numbers()
# print(next(gen))  # 0
# print(next(gen))  # 1
# print(next(gen))  # 2

# nums = [1, 2, 3, 4]
# squares = [x*x for x in nums]
# print(squares)  # [1, 4, 9, 16]


# def chaos(a, b, *args, **kwargs):
#     print(a, b)
#     print("args:", args)
#     print("kwargs:", kwargs)

# chaos(10, 20, 30, 40, fruit="mango", vibe="chill")


class Student:
 # static variable
 college = 'Manipal'
 def __init__(self):
 # instance variable declaration
    self.name = "ankit"
    self.age = 20
    self.roll_no = "23FE10CAI0026"
s = Student()
print(s.name)
print(s.age)
print(s.roll_no)