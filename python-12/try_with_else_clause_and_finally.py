def main():
    try:
       a = int(input("enter a number"))
       print(a)
       return 
    except Exception as e:
       print(e)
       return

# else:
#     print("I am inside an else") # else ke andar tab jaata hai agar try successful tha 

    finally:
        print("I am inside of finally ") # finally runs at any time 
main()