# Author: Vivek Shangari

def main():
    myMessage = input('What is the plaintext? ')
    myKey = int(input('What is the key? '))
    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|')

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    #print("Entered Encryption block of tpcEncrypt.py")
    #print("Key value:", key , "plaintext:" , message)
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the
            # end of the current column in the ciphertext list.
            ciphertext[column] += message[currentIndex]

            # move currentIndex over
            currentIndex += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
# if __name__ == '__main__':
main()