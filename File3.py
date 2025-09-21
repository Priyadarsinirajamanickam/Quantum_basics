#class 5
#Question 2 : Using for loop# 
#To get an input message from user 
#and print the statement in one line

#get an input message from user
print('This is a for loop program to execute message in single line')
message = input('What is your message? ')

#to print the characters of the message in multiple lines
for a in range (len(message)):
    print(message[a])


#to print the characters of the message in single line
for a in range (len(message)):
    print(message[a],end ='')

#to print the index values
#for a in range (len(message)):
#    print(a,end ='')

#prints the result,but ends with %
#'%' symbol represents the end of message/statement