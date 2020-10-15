import random

number = random.randint(1,10)

name = input (("Hey there, what's your name? "))

print ("Nice to meet you " + name + " please pick a number between 1 and 10. ")

def main():  
  guess = int(input("Ready, Set, Go....? "))
  if guess == number:
    print ("Good Job " + name + ", you must be a mind reader.")
  elif guess == 0:
    print ("Not between 1 and 10, is it?")
  elif guess == (number+1):
    print("OOOOooooh, just a tad to high.")
  elif guess == (number-1):
    print("NEARLY! Just a bit too low.")
  elif guess == (number+2):
    print("No... too high. ")
  elif guess == (number-2):
    print("No... too low. ")
  elif guess == (number-3):
    print("Nah, but not a terrible guess.  ")
  elif guess == (number+3):
    print("Nah, but not a terrible guess.  ")
  elif guess == (number-4):
    print("Not a million miles away. ")
  elif guess == (number+4):
    print("Not a million miles away. "
  #elif guess == (number - 5):
   # print("Nope. ")
  #elif guess == (number+5):
   # print("Nope. ")
  elif guess == (number-6):
    print("Definitely not the right answer. ")
  elif guess == (number+6):
    print("Definitely not the right answer. ")
  elif guess == (number-7):
    print("Not even close.")
  elif guess == (number+7):
    print("Not even close.")
  elif guess == (number-8):
    print("So far away. ")
  elif guess == (number+8):
    print("So far away. ")
  elif guess == (number-9):
    print("You couldn't be further from the right answer if you tried.")
  elif guess == (number+9):
    print("You couldn't be further from the right answer if you tried.")
  else: 
    print("We both know that's not what I'm looking for here.")

  yesList = ["Yes", "Y", "y", "Yeah", "yes"]
  noList = ["No", "N", "n", "Nah", "no"]
def restart():
  max_tries = 6
  while max_tries >0:
  restart = input ("Would you like to try again? ")
  if restart in yesList:
    main()
  elif restart in noList:
    print ("GoodBye. ")
  else:
    print ("It's like that is it? Good Bye then, " +name + ".")
  restart()
main()
