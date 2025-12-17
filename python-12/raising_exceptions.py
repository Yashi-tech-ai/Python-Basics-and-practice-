a = int(input("enter a number : "))
b = int(input("enter a number : "))
if(b == 0):
    raise ZeroDivisionError("hey our progrmas cannot run when dividing by zero")
else: 
  print(f"{a/b}")