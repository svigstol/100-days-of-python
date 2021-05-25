# 100 Days of Python
# Day 8 - Caesar Cipher
# Sarah Vigstol
# 5/23/21

import ascii

# list of letters a through z
alphabet = list(map(chr, range(97, 122))) + list(map(chr, range(97, 122)))

print(ascii.logo)

print("What would you like to do?")
print("Type 'encode' to encrypt or 'decode' to decrypt.")
userAction = input("> ").lower()

print("Enter your message: ")
userInput = input("> ").lower()

print("Enter the shift number: ")
shiftNumber = int(input("> "))

def caesar(userInput, shiftNumber):
    if userAction == 'encode':
        plainText = userInput
        shift = shiftNumber
        encodedText = ""
        for letter in plainText:
            listPosition = alphabet.index(letter)
            newPosition = listPosition + shift
            newLetter = alphabet[newPosition]
            encodedText += newLetter
        print(f"The encoded message is: {encodedText}")
    elif userAction == 'decode':
        encodedText = userInput
        shift = shiftNumber
        decodedText = ""
        for letter in encodedText:
            listPosition = alphabet.index(letter)
            newPosition = listPosition - shift
            newLetter = alphabet[newPosition]
            decodedText += newLetter
        print(f"The decoded message is: {decodedText}")

caesar(userInput, shiftNumber)
