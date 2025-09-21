# Author: Vivek Shangari
#Caeser cipher Tester program
import random, sys, CCEncryption, CCDecryption

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
        print("Plain text:",myMessage)
        #print(i+1,myMessage +'|',"len(m)",len(myMessage))

        encrypted = CCEncryption.encryptionB(myKey, myMessage,'e')
        print("Encrypted: ",encrypted)
        decrypted = CCDecryption.decryptionB(encrypted, myKey,'d')
        print("Decrypted: ",decrypted)
#        # The string to be encrypted/decrypted:

# #mode = input('Would you like to encrypt (e) or decrypt (d)? ')

# # Whether the program encrypts or decrypts:
# # mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

# # Every possible symbol that can be encrypted:
# # Please don't change the value held by variable SET
#     SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()_<>?/.,"

# # Stores the encrypted/decrypted form of the message:
#     translated = ''

#     for symbol in message:
#     # Note: Only SET in the `SET` string can be encrypted/decrypted.
#         if symbol in SET:
#             symbolIndex = SET.find(symbol)

#         # Perform encryption/decryption:
#             '''if mode == 'e':
#                 translatedIndex = symbolIndex + myKey
#             elif mode == 'd':
#                 translatedIndex = symbolIndex - myKey'''

#         # Handle wrap-around, if needed:
#             if translatedIndex >= len(SET):
#                 translatedIndex = translatedIndex - len(SET)
#             elif translatedIndex < 0:
#                 translatedIndex = translatedIndex + len(SET)

#             translated = translated + SET[translatedIndex]
#         else:
#         # Append the symbol without encrypting/decrypting:
#             translated = translated + symbol

# # Output the translated string:
#         print(translated)

        # If the decryption doesn't match the original message, display
        # an error message and quit.
        if myMessage != decrypted:
                print('Mismatch with key %s and message %s.' % (myKey, myMessage))
                print('Decrypted as: ', decrypted)
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
#if __name__ == '__main__':
main()
