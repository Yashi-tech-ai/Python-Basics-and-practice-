class employee:
    a = 1
class programmer(employee):
    b = 3
class manager(programmer):
    c = 2

o = employee()
print(o.a)# this will show a = 1 as this attribute is in employee
o = programmer()
print(o.a,o.b)
o = manager()
print(o.a,o.b,o.c)
