import Crypto.Util.number
import sys

bits=20

if (len(sys.argv)>1):
        bits=int(sys.argv[1])

print ("No of bits in prime is ",bits)

p=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print ("\nRandom n-bit Prime (p): ",p)

q=Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print ("\nRandom n-bit Prime (q): ",q)

N=p*q

print ("\nN=p*q=",N)

PHI=(p-1)*(q-1)

print ("\nPHI (p-1)(q-1)=",PHI)

e=65537
print ("\ne=",e)
d=Crypto.Util.number.inverse(e,PHI)
print ("d=",d)

print ("\nCount of decimal digits (p): ",len(str(p)))
print ("Count of decimal digits (N): ",len(str(N)))

M=56
print ("\n\n=== Let's try these keys ==")
print ("\nRSA Message: ",M)
enc=pow(M,e,N)
print ("RSA Cipher(c=M^e mod N): ",enc)
dec = pow(enc,d,N)
print ("RSA Decipher (c^d mod N): ",dec)

RootN = int(pow(N, 0.5))

if (RootN % 2 == 0):
    RootN = RootN + 1
    
print (RootN)

odd_test = RootN

while (odd_test > 1):
    mod_test = (N % odd_test)
    if (mod_test == 0):
        prime1 = odd_test
        prime2 = int(N/odd_test)
        print (prime1, prime2)
        odd_test = 0
    else:
        odd_test = odd_test - 2
