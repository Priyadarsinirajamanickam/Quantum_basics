#Class 5
#Question 6:Backward cipher: Ceaser cipher +Reverse cipher combination

'''Problem 3: The Backwards Cipher
Focus: for loop, in, find(), character-by-character logic (no slicing, no range())

A secret agent has intercepted a Caesar-encrypted message that was transmitted in reverse order — that is, the last letter of the message was sent first.

Your job is to:
Read the encrypted message (uppercase)
Read the Caesar key (a positive integer)
Decrypt it using the Caesar Cipher decryption logic by reading the message from end to start
Print the final decoded message

Constraints:
Do not use slicing ([::-1])
Do not use the range() function
Use a regular for loop or a while loop to reverse-read the message
Use only concepts seen in the original Caesar Cipher code: for, in, find, string concatenation

Example:
Input message: YXWVUT
Key: 5
Output: BANANA'''


#copied base content from Ceaser cipher & Reverse cipher
print('This is a program to execute Backwards Cipher')
a = input('What is your encrypted text message? ')
key = int(input("What is your key? "))
aftertranslation = '' 
i = len(a) -1 
while i >= 0: #condition provided
    aftertranslation = aftertranslation + a[i] 
    i = i-1 
print("Reversed Cipher: ",aftertranslation)
SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()_<>?/.,"
translated =''


#adding the output of reverse program into caeser cipher
#to decrypt by default
for symbol in aftertranslation:
    if symbol in SET:
        symbolIndex = SET.find(symbol)
        translatedIndex = symbolIndex - key

        # Handle wrap-around, if needed:
        if translatedIndex < 0:
            translatedIndex = translatedIndex + len(SET)

        translated = translated + SET[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print("Original message: ",translated)
