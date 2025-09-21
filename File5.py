#class 5
#Question: 4
'''Problem 2: Frequency Finder
Focus: find() method + counting + for loop

You're analyzing a message to detect how often each letter in SET appears.

Task:
Take a message (uppercase) as input
Loop through each letter in the Caesar Cipher SET
For each letter, count how many times it appears in the message using a for loop and if condition
Print each letter and its frequency, but only if it appears at least once
Constraints:
Don't use .count() method.
Use find() for comparison or positioning logic if needed.

Example:
Input message: ATTACK AT DAWN
Output:
A: 3
T: 3
C: 1
K: 1
D: 1
W: 1
N: 1'''
#get an input message from user
print('This is a program on Frequency Finder')
message = input('What is your message? ')

SET ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#to get the Character in input and print it on screen in order
for symbol in message:
    if symbol in SET:
        symbolIndex = SET.find(symbol) 
        occurence = 0 #dummy variable set to 0
#to get the n times the variable in input message
        for alpha in message:
          if alpha ==symbol:
             occurence = occurence +1
             
        '''else:# did not work with else block
             occurence =1''' #as it sets occurence to 1 ,everytime
                              #the alpha is not matched
        if occurence >0:
           print(symbol,occurence)    
   
    
    #still it prints character by character and 
    # not as expected

    #print(SET[symbolIndex],occurence) 
    #prints the same as above
      
    

