# we can simplify the process of printing values from a list rather than using for loop by using enumerate
l = [23,45,56,56,76,87,]

for index , item in enumerate(l):
    print(f"The item number at {index} is {item}")
     