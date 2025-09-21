import random
import cryptomath , detectEnglish

#Encryption alone

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB):
    if keyA and keyB:
        while keyA == 1 or keyB == 0 or keyA < 0 or keyB < 0 or keyB >= len(SYMBOLS) or cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
            keyA, keyB = getKeyParts(getRandomKey())
    return keyA, keyB

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    keyA, keyB = checkKeys(keyA, keyB)  # Ensure valid key parts
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol
    # Return both ciphertext and recomputed key
    finalKey = keyA * len(SYMBOLS) + keyB
    print(ciphertext+ '|',finalKey)
    return ciphertext, finalKey



def main():
    print("This is Affine cipher Encryption program")
    myMessage = input('What is the message? ')
    myKey  = getRandomKey()
    encryptMessage(myKey, myMessage)
    
#main()

