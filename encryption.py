import random,math

key = 0

def encrypt(inputText):
    key = str(random.randint(1000000000,9999999999))
    keyIndex = 0
    outputText = ""
    for letter in inputText:
        letter = ord(letter)-96
        letter = letter + int(key[keyIndex])
        keyIndex += 1
        outputText += str(letter)
    return outputText

def decrypt(inoutText):
    keyIndex = 0
    outputText = ""
    tempLetter = ""
    for letter in inoutText:
        tempLetter = letter - key[keyIndex]
        tempLetter = chr(letter + 96)
        outputText += tempLetter
    return outputText

encrypted = encrypt("jai")
print(decrypt(encrypted))