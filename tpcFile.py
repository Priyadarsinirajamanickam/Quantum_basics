# Author: Vivek Shangari

import time, os, sys, tpcEncrypt, tpcDecryptP

def main():
    inputFilename = 'Encrypted.txt'
    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file.
    outputFilename = 'Decrypted.txt'
    myKey = int(input('What key to use? '))
    myMode = input('Encrypt (e) or Decrypt (d): ')

    # If the input file does not exist, then the program terminates early:
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    # Read in the message from the input file:
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long the encryption/decryption takes:
    startTime = time.time()
    if myMode == 'e':
        translated = tpcEncrypt.encryptMessage(myKey, content)
    elif myMode == 'd':
        translated = tpcDecryptP.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # Write out the translated message to the output file:
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


main()

#Error for pdf file:
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe2 in position 10: 
#invalid continuation byte

#Error for doc file:
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd0 in position 0: 
# invalid continuation byte

#supports .txt, XML and HTML
#no encryption happened for .xml & .html file 
#but file got generated. Unable to open file.

#