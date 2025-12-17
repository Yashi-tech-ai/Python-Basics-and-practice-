def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
print("Enter a number : ")
a = int(input())
multiplication_table(a)