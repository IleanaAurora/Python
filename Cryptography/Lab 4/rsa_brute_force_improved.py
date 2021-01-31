import Crypto.Util.number
import sys
import math
import time

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
start_time = time.time()
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
        print("--- %s seconds taken to execute ---" % (time.time() - start_time))
    else:
        odd_test = odd_test - 2

print ("\n\n=== My attempt at RSA semi-prime factorization ==\n")
start_time = time.time()

def FermatFactor(N):
    a = math.ceil(math.sqrt(N))
    print("The root of N is",a)
    b2 = a*a-N
    root = math.sqrt(b2)
    possibleSquare = int(root + 0.5) ** 2
    while possibleSquare != b2:   #repeat until b2 is a square
            a += 1
            b2 = a*a-N
            root = math.sqrt(b2)
            possibleSquare = int(root + 0.5) ** 2
    primes = [int(a - math.sqrt(b2)),int(a + math.sqrt(b2))]
    return primes

answer = FermatFactor(N)
print("The primes are",answer)
print("--- %s seconds taken to execute ---" % (time.time() - start_time))
