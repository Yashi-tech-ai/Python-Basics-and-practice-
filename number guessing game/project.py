print("Lets play a number guessing game ." \
" The computer will generate a randon number and you will have to guess it . Good luck !")
import random
r = random.randint(1,100)
a = -1 
no_of_guess = 0
while( a != r):
   a = int(input("Enter a number between 1 to 100 : "))
   if(a == r):
      print("yahhh you have guessed the correct number")
      no_of_guess += 1
   elif(a < r):
      print("Guess a number higher from your previous input")
      no_of_guess += 1
   elif(a > r):
      print("Guess a number lower than your previous input")
      no_of_guess += 1
   else:
      print("oops wrong input")
print(f"You have guessed the correct number in {no_of_guess} number of guesses. ")
      
