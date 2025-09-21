#To get the cipher and decrypt instantly.

import time
import detectEnglish, tpcDecryptP ,CCDecryption, AFC_Decryption


def reverseCipher(message):
    a = message
    i = len(message) -1
    translated = ''
    while i >= 0:
        translated = translated+ a[i]
        i = i-1
    #print(translated)
    if detectEnglish.isEnglish(translated, 50):
            totalTime = round(time.time() - startTime, 3)
            print('\n')
            print("Reverse Cipher")
            print("Decrypted text: ", translated)
            print('Test time: %s seconds, ' % (totalTime))
    
            return  # Stop after first correct decryption
    

def hacktpc(message):
    for key in range(1,len(message)):
        decryptedText = tpcDecryptP.decryptMessage(key, message)
        #print("TPC", decryptedText)
        if detectEnglish.isEnglish(decryptedText, 90):
            totalTime = round(time.time() - startTime, 3)
            print('\n')
            print("Transposition Cipher")
            print('Test time: %s seconds, ' % (totalTime))
            print("key:" ,key)
            print("Decrypted text: ", decryptedText)
    
            return  # Stop after first correct decryption


SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]|:;<>,.?/'

def hackCC(message):
    for key in range(1,len(SYMBOLS)):
        decryptedText, Key = CCDecryption.decryptionB(message, key, 'd')
        #print("cc:" , decryptedText)
        if detectEnglish.isEnglish(decryptedText, 95):
            totalTime = round(time.time() - startTime, 3)
            print('\n')
            print("Caesar Cipher")
            print('Test time: %s seconds, ' % (totalTime))
            print("key:" ,Key)
            print("Decrypted text: ", decryptedText)
    
            return  # Stop after first correct decryption

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'   
def hackAC(message):
    result = AFC_Decryption.hackAffine(message)
    if result is not None:
        decryptedText, key = result
        print("Decrypted Text:", decryptedText)
        print("Key used:", key)
    else:
        print("Failed to decrypt the message. No valid key found.")

    return

def main():
    global startTime
    message = input('Enter the encrypted message to hack: ')
    startTime = time.time()
    reverseCipher(message)
    hacktpc(message)
    hackCC(message)
    hackAC(message)
main()


               