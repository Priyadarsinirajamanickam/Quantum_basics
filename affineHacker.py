# Affine Cipher Hacker
# Author: Vivek Shangari

import affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    myMessage = "8Odo6dqL dLW76L XdW61wdhq6MdjdL77lm6 O"

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')


def hackAffine(message):
    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if detectEnglish.isEnglish(decryptedText, 95):
                return decryptedText, key
    #print("Key: ", key)
    return decryptedText, key
        

# If affineHacker.py is run (instead of imported as a module)
# call the main() function.
#if __name__ == '__main__':

main()