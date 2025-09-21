#class 5
#Question 1 : To get an input message from user and reverse 
# only one half of the message taking the input L or R again from user


#get an input message from user
print('This is a program to execute Reverse Cipher')

# Get input
message = input('What is your input message? ')
length = len(message)
half = length // 2

left = ''
right = ''
count = 0

# Manually build left and right halves
for char in message:
    if count < half:
        left = left + char
    else:
        right = right + char
    count += 1

# Ask user which half to reverse
reverse = input('You want Left reverse(L) or Right reverse(R)? ').upper()

aftertranslation = ''
if reverse == 'L':
    # Manually reverse left
    index = len(left) - 1
    while index >= 0:
        aftertranslation = aftertranslation + left[index]
        index -= 1
    aftertranslation += right

elif reverse == 'R':
    # Manually reverse right
    index = len(right) - 1
    while index >= 0:
        aftertranslation = aftertranslation + right[index]
        index -= 1
    aftertranslation = left + aftertranslation

else:
    print("Invalid input. Please enter L or R.")
    exit()

print("Here is your cipher:", aftertranslation)






















'''
print('This is a program to execute Reverse Cipher')
message = input('What is your input message? ')
i = len(message)//2

left =''
right =''
for a in range(0,i+1):
  #print(a)
  for j in message:
    left = left + j
#print(left)
#print(right)
aftertranslation =''
#length of string -1 to reverse the string
leftreverse = len(left) -1  
rightreverse = len(right)-1
#integer value is stored in above variables

reverse = input('You want Left reverse(L) or Right reverse(R)')
if reverse in 'L':
    
    while leftreverse>=0:
       aftertranslation = aftertranslation + left[leftreverse]
       leftreverse = leftreverse -1
       print("Here is your cipher",aftertranslation + right)
else: 
    while rightreverse >= 0:
       aftertranslation = aftertranslation + right[rightreverse]
       rightreverse = rightreverse -1
       print("Here is your cipher", left + aftertranslation)
       '''
