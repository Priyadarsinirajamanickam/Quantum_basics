#Class 4
#Reverse cipher assignment

#get an input message from user
print('This is a program to execute Reverse Cipher')
a = input('What is your message? ')

#creating a variable to store the reverse order of the input
aftertranslation = '' #empty value so as to 

i = len(a) -1 
# -1 //as the index value starts from 0 and 
# setting it to last index value to reverse the input

#using while loop
while i >= 0: #condition provided
    aftertranslation = aftertranslation + a[i] 
    #1st time override happens;2nd time concatenates the value
    i = i-1 #to make the loop run one more time

print("Your reverse Cipher is: |",aftertranslation)
# end of program