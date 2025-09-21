#To get the cipher and decrypt instantly.

import time
import detectEnglish, tpcDecryptP


def hack(message):
    for key in range(1,len(message)):
        decryptedText = tpcDecryptP.decryptMessage(key, message)
        if detectEnglish.isEnglish(decryptedText, 85):
            totalTime = round(time.time() - startTime, 3)
            print('\n')
            print('Test time: %s seconds, ' % (totalTime), "key:" ,key)
            print("Decrypted text:", decryptedText)
    
            return  # Stop after first correct decryption

def main():
    global startTime
    message = input('Enter the encrypted message to hack: ')
    startTime = time.time()
    hack(message)


main()

               