def myfunc():
    print("Hello World!!")


if __name__ == "__if_name_main__":
    # if this code is ran by its own file its present in 
    print("We are directly running this code ")
    myfunc()
    print(__name__)