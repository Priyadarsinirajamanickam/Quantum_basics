# affineDecryptHack.py
import detectEnglish

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def decryptMessage(keyA, keyB, message):
    modInverseKeyA = findModInverse(keyA, len(SYMBOLS))
    if modInverseKeyA is None:
        return None
    decrypted = ''
    for symbol in message:
        if symbol in SYMBOLS:
            index = SYMBOLS.find(symbol)
            decryptedIndex = (index - keyB) * modInverseKeyA % len(SYMBOLS)
            decrypted += SYMBOLS[decryptedIndex]
        else:
            decrypted += symbol
    return decrypted

def hackAffine(ciphertext):
    for keyA in range(2, len(SYMBOLS)):
        if gcd(keyA, len(SYMBOLS)) != 1:
            continue
        for keyB in range(len(SYMBOLS)):
            decrypted = decryptMessage(keyA, keyB, ciphertext)
            if detectEnglish.isEnglish(decrypted, 90):
                key = keyA * len(SYMBOLS) + keyB
                return decrypted, key             
    print("❌ Failed to decrypt.")

def main():
    message = input("Enter encrypted message to decrypt: ")
    decrypted, key =hackAffine(message)
    print(decrypted+ '|', key) 

#if __name__ == '__main__':
#main()
