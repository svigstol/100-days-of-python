# 100 Days of Python
# Day 8 - Caesar Cipher
# Sarah Vigstol
# 5/23/21

def caesar(userInput, shiftNumber):
    if userAction == 'encode':
        plainText = userInput
        shift = shiftNumber
        encodedText = ""
        for letter in plainText:
            if letter in alphabet:
                listPosition = alphabet.index(letter)
                newPosition = listPosition + shift
                newLetter = alphabet[newPosition]
                encodedText += newLetter
            else:
                encodedText += letter
        print(f"The encoded message is: {encodedText}")
    elif userAction == 'decode':
        encodedText = userInput
        shift = shiftNumber
        decodedText = ""
        for letter in encodedText:
            if letter in alphabet:
                listPosition = alphabet.index(letter)
                newPosition = listPosition - shift
                newLetter = alphabet[newPosition]
                decodedText += newLetter
            else:
                decodedText += letter
        print(f"The decoded message is: {decodedText}")

# list of letters a through z
alphabet = list(map(chr, range(97, 122))) + list(map(chr, range(97, 122)))

import ascii
print(ascii.logo)

allDone = False
while not allDone:
    print("What would you like to do?")
    print("Type 'encode' to encrypt or 'decode' to decrypt.")
    userAction = input("> ").lower()

    print("Enter your message: ")
    userInput = input("> ").lower()

    print("Enter the shift number: ")
    shiftNumber = int(input("> "))
    shiftNumber = shiftNumber % 26

    caesar(userInput, shiftNumber)

    print("Try again? Type 'yes' or 'no' to continue.")
    retry = input("> ").lower()
    if retry == "no":
        allDone = True
        print("Goodbye!")
