#program -Transposition decrypt

def main():

    myMessage = input('What is the Cipher text? ')
    myKey = int(input('What is the key? '))

    plaintext = decryptMessage(myKey, myMessage)
    print("Decrypted message: '" + plaintext + "'") 

def decryptMessage(key, message):
    #print("Entered Decryption block from tpcDecrypt.py file")
    #print("Key value:", key , "Cipher:" , message)
    ncolumns = key #do not performing 90 deg rotation
    nrows = len(message) // key
    if len(message) % key > 0:
        nrows += 1 #using augumented operator
    #   nrows = nrows +1

    shaded_boxes = (ncolumns * nrows) - len(message)
    # Create an empty grid
    cells = [[''] * ncolumns for _ in range(nrows)]
    #print(cells)
    index = 0
    for col in range(ncolumns):
        for row in range(nrows):
            # Skip shaded boxes at the bottom-right of the grid
            if col >= ncolumns - shaded_boxes and row == nrows - 1:
                continue
            if index < len(message):
                cells[row][col] = message[index]
                index += 1
                #print(cells)

    # Read the grid row-wise
    plaintext = ''
    for row in cells:
        plaintext += ''.join(row)

    return plaintext

main()

#find greyed boxes
    #if len(message)== int(key):
    #    greyed = 0
    #else:
    #    greyed= (key*(q+1))-len(message)