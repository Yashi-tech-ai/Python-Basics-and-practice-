# f = open("my.txt")
# content = f.read()
# if("twinkle" in content):
#     print("Twinkle is present")
# else:
#     print("no its not")
# f.close()


# import random
# def game():
#     print("You are playing a game: ")
#     score = random.randint(1, 62)
#     # fetch the highscore
#     try:
#         with open("highscore.txt", "r") as f:
#             hiscore_str = f.read().strip()  # removes spaces/newlines
#             if hiscore_str:  # if it's not empty
#                 hiscore = int(hiscore_str)
#             else:
#                 hiscore = 0 # if empty 
#     except FileNotFoundError:
#         hiscore = 0
#     print(f"{score} is the current score")
#     if score > hiscore:
#         print("🎉 New high score!")
#         with open("highscore.txt", "w") as f:
#             f.write(str(score))
#     return score

# game()



# def table():
#     # Create and write tables from 2 to 20
#     with open("my.txt", "w") as f:
#         for i in range(2, 21):
#             f.write(f"Table of {i}:\n")
#             for j in range(1, 11):
#                 f.write(f"{i} x {j} = {i*j}\n") # = table
#             f.write("\n")  # Add a newline after each table
# # with open("Tables/Tables{n}.txt","w"): this way we can create folder named table and then generate individual tables.txt
# #    f.write(table)

#     # Now read and print the file content
#     with open("my.txt", "r") as f:
#         content = f.read()
#         print(content)
# table()

     

# with open("my.txt","r") as f:
#     content = f.read()
#     st = ["donkey","moneky","is"]
#     for word in st:
#       content = content.replace(word, "#"*len(word))
#       content = content.replace(word.capitalize(), "#"*len(word))
#       content = content.replace(word.upper(), "#"*len(word))
# with open("my.txt","w") as f:
#     f.write(content)
# with open("my.txt", "r") as f:
#     print(f.read())


# with open("log.txt","r") as f:
#     word = "Python"
#     content = f.read()
#     if((word.lower() or word.capatalize())in content):
#         print(f"Yes the {word} exists in log file ")
#     else:
#         print("Nah bro you good")


# with open("log.txt","r") as f:
#     word = "Python"
#     lines = f.readlines()
#     lineno = 1
#     for line in lines:
#       if(word.lower() in line.lower()):
#          print(f"Yes the {word} exists in log file . line no. = {lineno}")
#          break # this will break loop and else won't execute 
#       lineno += 1
#     else:
#         print("Nah bro you good")



# with open("log.txt", "r") as f:
#     content = f.readlines()
# with open("this.txt", "w") as f:
#     for line in content:
#         f.write(line)


# with open("log.txt") as f:
#     content1 = f.readlines()
# with open("this.txt") as f:
#     content2 = f.readlines()
# if(content1 == content2):
#     print("Bro they twining")
# else:
#     print("Nah bro they cool")


with open("this.txt","w") as f:
    f.write("")