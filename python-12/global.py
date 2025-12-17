a = 50 # global variable which runs through the whole code 

def fun():
    # global a # it is to change the global variable 
    a = 4 # local variable cause it runs only in the function 
    print(a)

fun()
print(a)