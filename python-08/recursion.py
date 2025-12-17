# def factorial(n):
#     if(n==0 or n== 1):
#         return 1
#     return n * factorial(n-1)

# print("Enter a number : ")
# n = int(input())
# print(factorial(n))


def sumation(n):
    if(n == 0 ):
        return 0
    return n + sumation(n-1)

print("Enter a number : ")
n = int(input())
result = sumation(n)
print(result)