# Simple number guessing game I got from a coding exercises book.

import random

secretNumber = random.randint(100,999)
secretList = [int(x) for x in str(secretNumber)]

guessCounter = 1
guessNumber = ""
guessList = []
response = ""
gameOver = False

print("""I am thinking of a three digit number. Try to guess what it is.
      Here are some clues:
      When I say:   That means:
      - Pico        - One digit is correct but in the wrong position.
      - Fermi       - One digit is correct and in the right position.
      - Bagles      - No digits are correct.
      I've thought of a number, and you have 10 guesses!""")

def listOverlap(a, b):
      for i in a:
            if i in b:
                  return True
      return False

while gameOver == False:
      response = "" # Just resetting

      guessNumber = input("Guess #" + str(guessCounter) +"\n> ")
      guessList = [int(y) for y in str(guessNumber)]

      if listOverlap(guessList, secretList) == True:
            for x in secretList:
                  if x in guessList:
                        if guessList.index(x) == secretList.index(x):
                              response += "Fermi "
                        else:
                              response += "Pico "
            if guessList == secretList:
                  response = "You guessed it in " + str(guessCounter) + " guesses! Good job!"
                  gameOver = True
      else:
            response = "Bagels"

      print(response)
      guessCounter += 1
      if guessCounter == 11:
            print("So close! The number I was thinking of was " + str(secretNumber) + ". Better luck next time!")
            gameOver = True
