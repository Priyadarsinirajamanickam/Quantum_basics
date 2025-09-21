# Author: Vivek Shangari

import sys, cryptomath, random
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def main():
    myMessage = input('What is the message? ')
    myKey = 4283
    myMode = input('Encrypt (e) or Decrypt (d)? ') # Set to either 'e' or 'd'.

    if myMode == 'e':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'd':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myKey))
    print(translated)


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        print('Cipher is weak if key A is 1. Getting Random keys.')
        KEY = getRandomKey()
        keyA, keyB = getKeyParts(KEY)
        #print('Key: %s' % (KEY))
    if keyB == 0 and mode == 'encrypt':
        print('Cipher is weak if key B is 0. Getting Random keys.')
        KEY = getRandomKey()
        keyA, keyB = getKeyParts(KEY)
        #print('Key: %s' % (KEY))
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        print('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
        KEY = getRandomKey()
        keyA, keyB = getKeyParts(KEY)
        #print('Key: %s' % (KEY))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        print('Key A (%s) and the symbol set size (%s) are not relatively prime. Getting Random keys.' % (keyA, len(SYMBOLS)))
        KEY = getRandomKey()
        keyA, keyB = getKeyParts(KEY)
        #print('Key: %s' % (KEY))

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'e')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol # Append the symbol without encrypting.
    return ciphertext


def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'd')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))
    for symbol in message:
        if symbol in SYMBOLS:
            # Decrypt the symbol:
            symbolIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # Append the symbol without decrypting.
    return plaintext


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

#main()