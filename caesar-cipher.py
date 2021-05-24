# 100 Days of Python
# Day 8 - Caesar Cipher
# Sarah Vigstol
# 5/23/21

# list of letters a through z
alphabet = list(map(chr, range(97, 122)))

print("What would you like to do?")
print("Type 'encode' to encrypt or 'decode' to decrypt.")
userAction = input("> ").lower()

#if userAction == 'encode' or userAction == 'decode':
#    # input ok
#    print('ok')
#else:
#    print("Invalid input. Please try again.")
#    print("What would you like to do?")
#    print("Type 'encode' to encrypt or 'decode' to decrypt.")
#    userAction = input("> ").lower()

print("Enter your message: ")
userInput = input("> ").lower()

print("Enter the shift number: ")
shiftNumber = int(input("> "))

def encrypt(plainText, shift):
    encodedText = ""
    for letter in plainText:
        listPosition = alphabet.index(letter)
        newPosition = listPosition + shift
        newLetter = alphabet[newPosition]
        encodedText += newLetter
    print(f"The encoded message is: {encodedText}")

def decrypt(plainText, shift):
    decodedText = ""
    for letter in plainText:
        listPosition = alphabet.index(letter)
        newPosition = listPosition - shift
        newLetter = alphabet[newPosition]
        decodedText += newLetter
    print(f"The decoded message is: {decodedText}")

if userAction == 'encode':
    encrypt(plainText=userInput, shift=shiftNumber)
else:
    decrypt(plainText=userInput, shift=shiftNumber)
