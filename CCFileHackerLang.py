# Author: Vivek Shangari

import time, os, sys, CCDecryption , detectEnglish

inputFilename = 'words.txt'
outputFilename = 'answer.txt'

def main():
    if not os.path.exists(inputFilename):
         print('The file %s does not exist. Quitting.' % (inputFilename))
         sys.exit()

    inputFile = open(inputFilename)
    content = inputFile.read()
    inputFile.close()

    hackedMessage = hackCC(content)

    if hackedMessage != None:
        print('Writing decrypted text to %s.' % (outputFilename))

        outputFile = open(outputFilename, 'w') # 'w' flag
        outputFile.write(hackedMessage)
        outputFile.close()
    else:
        print('Failed to hack encryption.')


def hackCC(message):
    print('Hacking...')
    for key in range(len(message)):

        startTime = time.time()

        decryptedText = CCDecryption.decryptionB(key, message, 'd')
        Boolean = detectEnglish.isEnglish(decryptedText, 95,85)

        
        if Boolean == True :
            totalTime = round(time.time() - startTime, 3)
            print('Test time: %s seconds, ' % (totalTime), end='')
            print("Is it English language? :", Boolean ,"Key:", key)
            return decryptedText
        
        

main()