# Pranav Abbaraju
# Cipher

def cipher(string, shift):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  newString = ""
  for x in range (len(string)):
    newString += alphabet[alphabet.find(string[x]) - shift]
  return newString

print cipher("abcdef", 1) 
print cipher("abcdef", 2)
print cipher("abcdef", 3)
print cipher("dogcatpig", 1)
print cipher("dogcatpig", 2)
print cipher("dogcatpig", 3)