# def greates_of_three_numbers():
#     a = int(input("Enter a number:"))
#     b =int(input("Enter a number:"))
#     c = int(input("Enter a number:"))
#     if(a > b and a > c):
#         print(f"{a} is greater number")
#     elif(b>a and b > c):
#         print(f"{b} is greater number")
#     else:
#         print(f"{c} is greater number")
# greates_of_three_numbers()


# def celcius_to_farehnite():
#     a = int(input("Enter the temperature in celcius :"))
#     farehnite = ((5/9)*(32-a))
#     print(f"The temperature in farehnite is : {round(farehnite,2)} degree F")
# celcius_to_farehnite()


# def sum_of_first_n_natural_numbers(n):
#     if n == 0:  # base case: sum of first 0 natural numbers is 0
#         return 0
#     return n + sum_of_first_n_natural_numbers(n - 1)
# print("Enter a number : ")
# a = int(input())
# print(f"The sum of first {a} natural numbers is {sum_of_first_n_natural_numbers(a)}")


# def right_angled_pyramid(n):
#     for i in range(n,0,-1):
#         print("*"*i)
# print("Enter a number : ")
# a = int(input())
# right_angled_pyramid(a)


# def inches_to_cm(inches):
#     cm = inches*2.54
#     print(cm)
# print("Enter a number : ")
# a = int(input())
# inches_to_cm(a)


# def multiplication_table(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
# print("Enter a number : ")
# a = int(input())
# multiplication_table(a)


def remove_list(substring_to_remove):
    l = ["yashi", "anay", "manish", "sarita", "grandparents"]
    print("Original list:", l)
    # Step 1: remove a full name based on user input
    name_to_remove = input("Enter the full name to remove from the list: ").strip().lower()
    l = [name for name in l if name.lower() != name_to_remove]
    # Step 2: remove the given substring (like "an") from all names
    updated_list = [name.replace(substring_to_remove, "") for name in l]
    print("Updated list:")
    print(updated_list)
# You’re calling it with "an" to remove "an" from every name
remove_list("an")
