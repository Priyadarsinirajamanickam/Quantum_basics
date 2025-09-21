x = int(input("Get a value for a: "))
y = int(input("Get a value for b: "))

def gcd(a,b):
    while (a !=0):
        a,b = b%a, a
    return b

print("GCD of ",x ,"," ,y ,"is: ", gcd(x,y))