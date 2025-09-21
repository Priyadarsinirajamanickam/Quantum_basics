# Author: Vivek Shangari
#program to test Transposition Cipher
import random, sys, tpcEncrypt, tpcDecryptP

def main():
    #random.seed(5)
    #myKey = 2 * random.randint(1,50)
    #print("Key value: ", myKey)
    for i in range(1,10):
        myKey = random.randint(1,20) 
        print("\n")
        print("------","text:",i,"-----")
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(1,5)
        message = list(message)
        random.shuffle(message)
        myMessage = ''.join(message)
        print("Plain text:", myMessage)
        #print(i+1,myMessage +'|',"len(m)",len(myMessage))

        encrypted = tpcEncrypt.encryptMessage(myKey, myMessage)
        decrypted = tpcDecryptP.decryptMessage(myKey, encrypted)
        print("Decrypted: ", decrypted)
        # If the decryption doesn't match the original message, display
        # an error message and quit.
        if myMessage != decrypted:
                print('Mismatch with key %s and message %s.' % (myKey, myMessage))
                print('Decrypted as: ' + decrypted)
                sys.exit()
    
        if myMessage == decrypted:
                print('Transposition cipher test passed.')
    print("\n")
    #print("plaintext used: ", myMessage)
    #print("Key used:", myKey)
    #print("Ciphertext: ", encrypted)
    #print("plaintext: ", decrypted)
    #print('Transposition cipher test passed.')


# If transpositionTest.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
