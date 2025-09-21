# Caesar Cipher program for random inputs
# Author: Vivek Shangari
# URL: https://acehacker.com/whois/vivek
import random
# The string to be encrypted/decrypted:

def main():
     for i in range(1,10):
        m='ed'
        mode = 'd'
        #random.seed(5)
        myKey = random.randint(1,20) 
        print("\n")
        print("------","text:",i,"-----")
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()_<>?/.,' * random.randint(1,5)
        message = list(message)
        random.shuffle(message)
        myMessage = ''.join(message)
        print("Input:", myMessage, "Key:", myKey)
        

        encryptionB(myKey,message,mode)
         
    
def encryptionB(Key,Message,mode):
        print("Entered E block")
       
        SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]|:;<>,.?/"

# Stores the encrypted/decrypted form of the message:
        translated = ''

        for symbol in Message:
    # Note: Only SET in the `SET` string can be encrypted/decrypted.
            if symbol in SET:
                symbolIndex = SET.find(symbol)

        # Perform encryption/decryption:
                if mode == 'e':
                    translatedIndex = symbolIndex + Key

        # Handle wrap-around, if needed:
                if translatedIndex >= len(SET):
                    translatedIndex = translatedIndex - len(SET)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SET)

                translated = translated + SET[translatedIndex]
            else:
        # Append the symbol without encrypting/decrypting:
                translated = translated + symbol
           
# Output the translated string:
        #print("Output:",translated)
        return translated  
#main()