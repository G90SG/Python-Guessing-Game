import random

number = random.randint(1,100)
##importing random directory and calling a random number between 1 and 100

name = input("Hello, What's your name? ")
print("Hey " + name + ", I'm thinking of a number between 1 & 100. Can you guess what it is?")
guess = int(input("Take a guess.. "))
#ask the user their name and ask them to take a guess

no_of_goes = 5
#define the variable (number of goes) and set up the while loop

while no_of_goes>1: 
  if (guess < number):
    print ("Oooh, too low")
    no_of_goes = no_of_goes - 1 
    print ("You have "+ str(no_of_goes)+" remaining.") 
    guess = int(input("Guess again... "))

  
  elif guess > number:
    print ("Too high, "+name+".")
    no_of_goes = no_of_goes - 1
    print("You have "+ str(no_of_goes)+" remaining.")
    guess = int(input("Guess again... "))
 
  elif guess == number:
    print ("WOAH, you're a mind reader! Well done, " +name+ ".")
    break

else:
  print("You are all out of goes, "+name+". The correct number was "+ str(number)+". Better luck next time.")
  

