class number:
    def __init__(self,n):
        self.n = n
    def __add__(self,num):
        return self.n + num.n
    
n = number(1)
m = number(5)
print(n+m)

# Expression	Python Internally Calls
# n + m	 n.__add__(m)
# n - m	 n.__sub__(m)
# n * m	 n.__mul__(m)
# n == m	n.__eq__(m)
#n/m = n.__truediv__(m)
#n // m = n.__floordiv__(m)
# __str__() = sets what get displayed upon calling str(object)
#__len__()
# __gt__ = greater than 