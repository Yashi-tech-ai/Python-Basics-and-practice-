# class programmers:
#      company = "Microsoft"
# def __init__(anay,name,language,salary):
#         anay.name = name 
#         anay.language = language
#         anay.salary = salary 

# yashi =  programmers("yashi", "python", 500000)
# print(yashi.name,yashi.language,yashi.salary)



# class calculator:
#     def __init__(anay,n):
#         anay.n  = n
#     def square(anay):
#         print(f"Square is {anay.n*anay.n}")
#     def cube(anay):
#         print(f"Cube is {anay.n*anay.n*anay.n}")
#     def square_root(anay):
#         print(f"Square root is {anay.n**1/2}")

# a = calculator(15)
# a.square()
# a.cube()
# a.square_root()
       

# class probelm:
#     attribute = "a"
# arc = probelm()
# #print(arc.attribute) # this prints a since instance attribute not present
# arc.attribute = "b"
# print(arc.attribute) # this prints b as now instance is introduced 
# print(probelm.attribute) # this prints a since its problem.attribute 




# class calculator:
#     def __init__(anay,n):
#         anay.n  = n
#     def square(anay):
#         print(f"Square is {anay.n*anay.n}")
#     def cube(anay):
#         print(f"Cube is {anay.n*anay.n*anay.n}")
#     def square_root(anay):
#         print(f"Square root is {anay.n**1/2}")
#     @staticmethod
#     def greet():
#         print("I am a mathematician")

# a = calculator(15)
# a.square()
# a.cube()
# a.square_root()
# a.greet()


# from random import randint
# class train:
#     def __init__(anay,trainno):
#         anay.trainno = trainno
#     def booking(anay,fro,to):
#         print(f"The ticket is booked in {anay.trainno} from {fro} to {to}")
#     def getstatus(anay):
#         print(f"The status of train {anay.trainno} is running on time ")
#     def getfare(anay,fro,to):
#         print(f"The ticket fare of the train {anay.trainno} from {fro} to {to} is {randint(250,1000)}")
# a = train(123456)
# a.booking("jaipur","delhi")
# a.getstatus()
# a.getfare("jaipur","delhi")
    

class employee: 
    language = "py"
    salary = 12000000
    
    def get_info(anay):
        print(f"The language is {anay.language} and salary is {anay.salary}") 
    @staticmethod 
    def greet():
         print("good morning pineapple ")   
Yashi = employee() 
print(Yashi.language, Yashi.salary)
Yashi.get_info() 
employee.greet()

    
        