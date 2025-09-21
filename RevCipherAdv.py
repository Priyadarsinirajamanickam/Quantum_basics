#class 22
#Question 1 : To get an input message from user and reverse 
# word by word as per the user input to start from last or first

print('This is a program to execute Reverse Cipher')

# Get input
message = input('What is your input message? ')
words = message.split(' ')

reverse = input('You want to start from Last (L) or First (F)? ').upper()

if reverse == 'F':
    index_range = range(len(words))
elif reverse == 'L':
    index_range = range(len(words)-1, -1,-1) #runs for +ve graph
else:
    print("Invalid input. Please enter L or F.")
    exit()

a= ''
count = 0
aftertranslation = ''
for i in index_range:
    word = words[i]
    
    # Add space before next word if it is not empty
    if a != '':
        a += ' '

    if i % 2 == 0:
        count = count +1
        L1 = ''
        index = len(word) - 1
        while index >= 0:
            L1+= word[index]
            index -= 1
        a += L1
    else:
        a += word

if reverse == 'L':
    j = len(a) -1 
    while j >=0:
        aftertranslation =aftertranslation + a[j]
        j = j-1
    print("Here is your cipher:", aftertranslation)
else:
    print("Here is your cipher:", a)
print("Count of words reversed in a",len(words) ,"string input is ", count)

'''
for i in range(len(m)):
        if i %2 == 0:
            m1 = m[i]
            print("m1",m1)
            if reverse == 'L':
                index = len(m1) - 1
                while index >= 0:
                    aftertranslation = aftertranslation + m1[index]
            
                index -= 1
            elif reverse == 'F':
                index = len(m1) - 1
                while index >= 0:
                    aftertranslation = aftertranslation + m1[index]
                index -= 1
            else:
                print("Invalid input. Please enter L or F.")
            
        else:
           m2 = m[i]
           print("m2",m2)
print("Here is your cipher:", aftertranslation)

'''