#Map = works for each element present
l = [1,2,3,4,5,6]

square = lambda x: x*x
sqaurelist = map(square,l)
print(list(sqaurelist))



#filter
# def even(n):
#     if(n%2 == 0):
#         return True
#     return False
# my = filter(even, l)
# print(tuple(my))


#reduce
# from functools import reduce
# add = lambda a,b: a+b
# print(reduce(add,l))
# l = [1,2,3,4,5,6] = 
# step 1 = 1+2 = 3
# step 2 = 3+3 = 6
# strp 3 = 6+4 =10
# step 4 = 10+5 = 15
# step 5 = 15+6 = 21