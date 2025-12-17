# class two_dimensional_vector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
    
#     def show(self):
#         print(f"The two dimensional vector is {self.i}i + {self.j}j ")
# class three_dimensional_vector(two_dimensional_vector):
#     def __init__(self, i, j,k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"The three dimensional vector is {self.i}i + {self.j}j + {self.k}k ")

# o = two_dimensional_vector(1,2)
# o.show()
# p = three_dimensional_vector(1,2,3)
# p.show()


# class animals:
#     def __init__(self):
#         self.a = "reptiles "
#         self.b = "friendly pets"
#         self.c = "wild animals "
#         print(f"These are the animals we have {self.a} , {self.b} and {self.c}")

# class pets(animals):
#     def __init__(self):
#         self.e = "dogs"
#         self.f = "cats"
#         print(f"These are the pet animals we have  {self.e} and {self.f}")
# class dogs(pets):
#     def  __init__(self):
#         print(f"A dog barks")

# o = animals()
# p = pets()
# q = dogs()


# class employee:
#     salary = 24000
#     increment = 80
#     @property
#     def salaryafterincrement(self):
#         return self.salary + self.salary*(self.increment/100)
#     @salaryafterincrement.setter
#     def salaryafterincrement(self,salary):
#         self.increment =  ((salary / self.salary ) -1) *100
# e = employee()
# # print(e.salaryafterincrement)
# e.salaryafterincrement = 28000
# print(e.increment)



# class complex:
#     def __init__(self,r,i):
#         self.r =r 
#         self.i = i
#     # a +ib * c + id = a*c + b*d
#     def __add__(self, c2):
#         return complex(self.r + c2.r , self.i + c2.i)
#     def __mul__(self,c2):
#         return complex(self.r * c2.r , self.i * c2.i)
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
    
# c1 = complex(1,2)
# c2 = complex(3,4)
# print(c1 + c2)
# print(c1 * c2)



# class vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k
#     # def __add__(self,v2):
#     #     result = vector(self.i + v2.i , self.j +v2.j , self.k +v2.k)
#     #     return result
#     def __mul__(self,v2):
#       result = (self.i * v2.i + self.j * v2.j + self.k * v2.k)
#       return result  
#     def __str__(self):
#         return f"vector ({self.i},{self.j}, {self.k})"

# v1 = vector(1,2,3)
# v2 = vector(4,5,6)
# # print(v1 + v2)
# print(v1 * v2)


# class vector:
#     def __init__(self,l):
#         self.l = l
#     def __len__(self):
#         return len(self.l)

# v1 = vector([1,2,3,4,5,6,7])
# print(len(v1))
#       OR 
# class vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __add__(self,v2):
#         result = vector(self.i + v2.i , self.j +v2.j , self.k +v2.k)
#         return result
#     def __str__(self):
#         return f"vector ({self.i},{self.j}, {self.k})"
#     def __len__(self):
#        return int((self.i**2 + self.j**2 + self.k**2) ** 0.5) # magnitudal distance from origin also used as length 

# v1 = vector(1,2,3)
# v2 = vector(4,5,6)
# a = (v1 + v2)
# print(a)
# print(len(a))

