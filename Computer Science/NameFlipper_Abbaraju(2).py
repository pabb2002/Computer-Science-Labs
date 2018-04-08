# Pranav Abbaraju
# Name Flipper

word = raw_input("Enter your full name: ")
print word[word.find(" ")+1:len(word)] + "," + " " + word[0:word.find(" ")]
