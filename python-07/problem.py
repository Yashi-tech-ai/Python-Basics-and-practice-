# i = int(input("Enter the number to print its table: "))
# j = 1
# for j in range(1,11):
#    print(f"{i} X {j} = {i * j}") #  formatted string literal.


# l = ["yashi", "Anay", "Sarita", "Manish"]
# for i in l:
#     if i.lower().startswith("s"):
#      print("Hello", i)


# i = int(input("Enter the number to print its table: "))
# j = 1
# while(j<=10):
#     print(f"{i} X {j} = {i * j}")
#     j+= 1


# i = int(input("Enter the number to find if it's either prime or not: "))
# if i <= 1:
#     print("Numbers less than or equal to 1 are neither prime nor composite.")
# else:
#     for j in range(2, (i // 2) + 1):
#         if i % j == 0:
#             print(f"{i} is composite")
#             break
#     else:
#         # This else belongs to the for loop, it runs only if the loop completes without a break
#         print(f"{i} is prime")



# i = int(input("Enter the number: "))
# j = 0
# sum = 0
# while(j<=i):
#     sum += j
#     j+= 1
# print(sum) 


# i = int(input("Enter the number: "))
# factorial = 1
# if(i==0):
#     print(factorial)
# else:
#     for j in range(1,i+1):
#       factorial = factorial*j
# print(factorial)


# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):# spaces are only being print on left side and then it switches to make stars and then to new line 
#     print(" "*(n-i),end ="") # doesn't move to next line by end=""
#     print("*"*(2*i-1),end ="")
#     print("")


# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):# spaces are only being print on left side and then it switches to make stars and then to new line 
#      print("*"*(i),end ="")
#      print("")


# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     if(i==1 or i == n):
#       print("*"*n,end="")
#     else:
#       print("*",end="")
#       print(" "*(n-2),end="")
#       print("*",end="")
#     print("") #Print nothing... but still move to the next line.”


n = int(input("Enter the number to write its reverse multiplication table:"))
for i in range(10,0,-1): # or (0,11)
    print(f"{n} x {i} = {n*i}") # or print(f"{n} x {11-i} = {n*(11-i)}")
print("")