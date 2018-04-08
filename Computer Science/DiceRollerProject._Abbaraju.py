#Pranav Abbaraju
#Dice Roller Project without arrays

from random import *

top = ""
midone = ""
midTwo = ""
midThree = ""
bottom = ""
score = 0

def diceRoller(num, top, midone, midTwo, midThree, bottom, score):  
  for x in range(0, num):
    r = randint(1,6)
    score += r
    
    top += diceTB()
    midone = midone + diceMidone(r)
    midTwo = midTwo + diceMidTwo(r)
    midThree = midThree + diceMidThree(r)
    bottom += diceTB()
  
  return top + "\n" + midone + "\n" + midTwo + " Your score is: " + str(score) + "\n" + midThree + "\n" + bottom
  
def diceTB():
  return "------- "
  
def diceMidone(randomInt):
  if randomInt == 1:
    return "|     | "
  elif randomInt == 2:
    return "|  o  | "
  elif randomInt == 3:
    return "|  o  | "
  elif randomInt == 4:
    return "| o o | "
  elif randomInt == 5:
    return "| o o | "
  elif randomInt == 6:
    return "| o o | "
    
def diceMidTwo(randomInt):
  if randomInt == 1:
    return "|  o  | "
  elif randomInt == 2:
    return "|     | "
  elif randomInt == 3:
    return "|  o  | "
  elif randomInt == 4:
    return "|     | "
  elif randomInt == 5:
    return "|  o  | "
  elif randomInt == 6:
    return "| o o | "
  
def diceMidThree(randomInt):
  if randomInt == 1:
    return "|     | "
  elif randomInt == 2:
    return "|  o  | "
  elif randomInt == 3:
    return "|  o  | "
  elif randomInt == 4:
    return "| o o | "
  elif randomInt == 5:
    return "| o o | "
  elif randomInt == 6:
    return "| o o | "

print diceRoller(int(raw_input("Enter the number of rolls: ")), top, midone, midTwo, midThree, bottom, score)    