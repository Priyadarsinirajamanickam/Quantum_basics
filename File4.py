#class 5
#Question 3 : 
'''Problem 1: Mysterious Disappearing Letters
Focus: for loop + in keyword

You're given a secret message and a list of forbidden characters. Your job is to remove every character in the message that appears in the forbidden list.

Task:
Take a message as input
Take a string of forbidden letters (uppercase)
Use a for loop and the in keyword to build a new string where all forbidden letters are removed
Constraints:
You must check each character in the message one by one.
Don’t use list comprehensions or slicing.
Example:
Input message: HELLO WORLD
Forbidden letters: LO
Output: HE WRD'''


#get an input message from user
print('This is a program on Mysterious disappearing of letters')
message = input('What is your message? ')

forbidden = 'PRIYA'
output ='' # so as to append the new values
for a in message:
##if a not in forbidden:
#   output = output + a
   if a in forbidden:
      output = output
   else:
       output = output + a    


print(output)
#worked
'''
print('This is a program on Mysterious disappearing of letters')
message = input('What is your message? ')

forbidden = 'PRIYA'
output ='' # so as to append the new values
for a in message:
  if a not in forbidden:
     output = output + a   


print(output)
'''