# Import the Random Module
import random
# Create a Variable Number and assign it a random number between 1-100
number = random.randint(1,100)
# Create a Variable Name and ask the user for input of their name
name = input("Hello, What's your name? ")
# Concatenate in a string, asking the useer to guess the random number between 1-100
print("Hey " + name + ", I'm thinking of a number between 1 & 100. Can you guess what it is?")
# Obtaining Integer input 
guess = int(input("Take a guess.. "))
# The user has 5 goes
no_of_goes = 5
# Create While Loop for number of goes, reducing the variable no_of_goes by 1 after each guess 
while no_of_goes > 1: 
# If the number is more than the guess, advise the user that their guess was too low 
  if (guess < number):
    print ("Oooh, too low")
# Reducing the no_of_goes by 1 
    no_of_goes = no_of_goes - 1 
    print ("You have "+ str(no_of_goes)+" remaining.") 
# Asking the user to guess again
    guess = int(input("Guess again... "))
# if the number is smaller than the guess, print a statement to advise the guess is too high before reducing no_of_goes by one and asking the user to try again 
  elif (guess > number):
    print ("Too high, "+name+".")
    no_of_goes = no_of_goes - 1
    print("You have "+ str(no_of_goes)+" remaining.")
    guess = int(input("Guess again... "))
# If the guess is correct before the no_of_goes has run out, the program is ended  
  elif (guess == number):
    print ("WOAH, you're a mind reader! Well done, " +name+ ".")
    break
# Else statement to print once the user has run out of goes. Advising the Random number which they had failed to guess correctly. 
else:
  print("You are all out of goes, "+name+". The correct number was "+ str(number)+". Better luck next time.")
  

