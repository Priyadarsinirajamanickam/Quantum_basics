#class 6
#Question 1: Caeser Hacker program
#to use only decrypting and run the program for entire len(message)
#ignored Key 0 as it will return the same input

print('This is a program to execute Hacker Cipher')
message = input("What's the message? ")
#SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()_<>?/.,"
SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]|:;<>,.?/"
print(len(SET))
for i in range(1,len(SET)):
    translated = ''

    for symbol in message:
        if symbol in SET:
            symbolIndex = SET.find(symbol)
            translatedIndex = symbolIndex + i#+1 did not work
            # Handle wrap-around, if needed:
            if translatedIndex >= len(SET):
             translatedIndex = translatedIndex - len(SET)

            translated = translated + SET[translatedIndex]
        else:
            translated = translated+ symbol 
    print(i,translated)

'''
for symbol in message:
         if symbol in SET:
          symbolIndex = SET.find(symbol)
          translatedIndex = symbolIndex + 1
         # Handle wrap-around, if needed:
         if translatedIndex >= len(SET):
            translatedIndex = translatedIndex - len(SET)
         elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SET)

         translated = translated + SET[translatedIndex]
else:
           translated = translated + symbol

# Output the translated string:
print(translated)


for symbol in translated:
    if symbol in SET:
        symbolIndex = SET.find(symbol)
        translatedIndex = symbolIndex + 1
         # Handle wrap-around, if needed:
        if translatedIndex >= len(SET):
            translatedIndex = translatedIndex - len(SET)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SET)

        translated1= translated1 + SET[translatedIndex]
        
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated1)'''
