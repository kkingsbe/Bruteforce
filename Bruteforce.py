import sys

import noahsEncryption,time
def Bruteforce():
    start = time.time()
    words = open("wordlist","r+").readlines()
    wordFound = False
    for word in words:
        if noahsEncryption.encrypt(word.strip("\n")) == True:
            print(word)
            wordFound = True
            break
    if wordFound == False:
        print("Password not in wordlist")
        BruteforceConcat()

    end = time.time()
    print("Completed in " + str((end - start) * 1000) + " milliseconds!")


def BruteforceConcat():
    start = time.time()
    words1 = open("wordlist", "r+").readlines()
    words2 = open("wordlist", "r+").readlines()
    wordFound = False
    for x in words1:
        for y in words2:
            print(x.strip("\n")+y.strip("\n"))
            if noahsEncryption.encrypt(x.strip("\n")+y.strip("\n")) == True:
                print((x + y).strip("\n"))
                wordFound = True
                break
    if wordFound == False:
        print("Password not in wordlist")

    end = time.time()
    sys.exit("Completed in " + str((end - start) * 1000) + " milliseconds!")

Bruteforce();