# Pranav Abbaraj
# Hangman

from random import *
from math import *

word = "hangman"
hang = 0
game = 1
over = 0
def letterChecker(letter):
	if word.find(letter) == -1:
			hang += 1
	else:
		for x in range(len(word)):
			output = ""
			output += word.find(letter)*" " + letter
			
letterChecker("a")
