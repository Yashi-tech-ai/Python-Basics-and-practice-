# try :
#     with open("1.txt") as f:
#         print(f.read)
# except Exception as e:
#     print(e)
    

# l = [23,34,65,76,78,45,23,223]
# for index , item in enumerate(l):
#     if(index == 2 or index ==4 or index == 7):
#         print(f"the item on {index} is {item}")

    
# a = (int(input("Enter the number to display its multiplication table")))
# multiplication_table_list = [a*b for b in range (1,11) ]
# print(multiplication_table_list)



# try:
#   a = int(input("enter a number "))
#   b = int(input("enter a number "))
#   print(a/b)
# except  ZeroDivisionError as e:
#   print("Infinite")
#   or 
#   a = int(input("enter a number : "))
# b = int(input("enter a number : "))
# if(b == 0):
#     raise ZeroDivisionError("hey our progrmas cannot run when dividing by zero")
# else: 
#   print(f"{a/b}")


# in continuation of problem 3 
a = (int(input("Enter the number to display its multiplication table")))
multiplication_table_list = [a*b for b in range (1,11) ]
with open("file.txt","a") as f:
    f.write(str(multiplication_table_list) + "\n") # The f.write() function only writes strings into files. 