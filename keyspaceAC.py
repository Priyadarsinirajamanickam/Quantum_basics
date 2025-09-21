import affineCipher, cryptomath

message = "Today is Monday, May 5th 2025."
counter =0

keyspaceB = len(affineCipher.SYMBOLS)
keyspaceA = keyspaceB * keyspaceB

for keyA in range(2, keyspaceA):
    key = keyA * len(affineCipher.SYMBOLS) +1 #by default, setting keyB to 1
    if cryptomath.gcd(keyA , len(affineCipher.SYMBOLS))== 1:
        counter = counter +1
        print(keyA, affineCipher.encryptMessage(key, message))

#AC_Key = KeyA + KeyB
#AC_Key = multiplicative key + addition key
#E(x)=(keyA⋅x+keyB)mod m