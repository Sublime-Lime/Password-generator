import random

alphabet = 'qwertyuiopasdfghjklzxcvbnm'
numbers = '1234567890'
symbols = '!@#$%^&*()'
includeAlphabet = False
includeNumbers = False
includeSymbols = False
totalLexicon = ""
passwordLength = 0
password = ""
randomNum = ""
while True:
    userInput = input("Include Alphabet(Y/N): ")
    if userInput.casefold() == "y":
        includeAlphabet = True
        break
    elif userInput.casefold() == "n":
        includeAlphabet = False
        break
    else:
        print("Enter valid input")
        userInput = input("Include Alphabet(Y/N): ")
while True:
    userInput = input("Include Numbers(Y/N): ")
    if userInput.casefold() == "y":
        includeNumbers = True
        break
    elif userInput.casefold() == "n":
        includeNumbers = False
        break
    else:
        print("Enter valid input")
        userInput = input("Include Numbers(Y/N): ")
while True:
    userInput = input("Include Symbols(Y/N): ")
    if userInput.casefold() == "y":
        includeSymbols = True
        break
    elif userInput.casefold() == "n":
        includeSymbols = False
        break
    else:
        print("Enter valid input")
        userInput = input("Include Symbols(Y/N): ")
if includeAlphabet:
    totalLexicon += alphabet
if includeNumbers:
    totalLexicon += numbers
if includeSymbols:
    totalLexicon += symbols
while True:
    userInput = input("Password Length: ")
    if userInput.isnumeric():
        passwordLength = int(userInput)
        break
    else:
        print("Enter valid input")
        userInput = input("Password Length: ")
for x in range(passwordLength+1):
    randNum = random.randint(0, len(totalLexicon))
    password += totalLexicon[randNum]
print("Password is", password)
