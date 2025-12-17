class employee:
    def __init__(self):
        print("i am a good girl 1")
    a = 1
class programmer(employee):
    def __init__(self):
        print("i am a good girl 2")
    b = 3
class manager(programmer):
    def __init__(self):
        super().__init__()
        print("i am a good girl 3")
    c = 2

# o = employee()
# print(o.a)# this will show a = 1 as this attribute is in employee
# o = programmer()
# print(o.a,o.b)
o = manager()
print(o.a)