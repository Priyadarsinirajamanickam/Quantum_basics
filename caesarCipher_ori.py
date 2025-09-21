# Caesar Cipher
# Author: Vivek Shangari
# URL: https://acehacker.com/whois/vivek

# The string to be encrypted/decrypted:
message = input("What's the message? ")

# The encryption/decryption key:
key = int(input('What key should I use? '))

mode = input('Would you like to encrypt (e) or decrypt (d)? ')

# Whether the program encrypts or decrypts:
# mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted:
# Please don't change the value held by variable SET
SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()_+-=[]|:;<>,.?/"

# Stores the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Note: Only SET in the `SET` string can be encrypted/decrypted.
    if symbol in SET:
        symbolIndex = SET.find(symbol)

        # Perform encryption/decryption:
        if mode == 'e':
            translatedIndex = symbolIndex + key
        elif mode == 'd':
            translatedIndex = symbolIndex - key

        # Handle wrap-around, if needed:
        if translatedIndex >= len(SET):
            translatedIndex = translatedIndex - len(SET)
            # print(translatedIndex)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SET)

        translated = translated + SET[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated +'|')
