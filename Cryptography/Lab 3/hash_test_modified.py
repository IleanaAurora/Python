import math
import hashlib
import random
import os

hash_byte_size = 2

def prehash(digits):
    #converting alphabetical string to binary string
    res = ''.join(format(i, 'b') for i in bytearray(digits, encoding ='utf-8'))
    #if binary string is less than 256 digits
    if len(res) < 256:
        #pad with random binary values (0 or 1) until 256 is reached
        n = 256 - len(res)
        randBits = rand_key(n)
        res += randBits
    #if binary length % 256 is greater or equal to zero
    elif len(res)%256 >= 0:
        #pad with binary vals until the length can be modded by 256 to equal 0
        padWith = 256 - len(res)%256
        padWithBin = rand_key(padWith)
        res += padWithBin
    #Using string slicing to split string into equal halves 
    res_first, res_second = res[:len(res)//2],res[len(res)//2:]
    #invert the digits in the second half of the string
    res_second = res_second.replace('0', '%temp%').replace('1', '0').replace('%temp%', '1')
    #switch and recombine the second and first half of the string
    res = res_second + res_first
    #convert string to bytes
    b = res.encode('utf-8')
    hasher.update(b)
    a = hasher.hexdigest(hash_byte_size)
    return(a)

#function to create a random binary string
def rand_key(p): 
    key1 = "" 
    for i in range(p):
        #randomly generate 0 or 1 and convert into string
        temp = str(random.randint(0, 1))
        key1 += temp 
    return(key1) 
    
hasher = hashlib.shake_256()
#read file contents
with open('attack.txt', 'r') as afile1:
    buf = afile1.read()
afile1.close()
a = prehash(buf)
print("The hex digit to match is",a)

collision = 0
max = pow(2, 64)
i = 0

while (i<max) & (collision == 0):
        #read file contents
        with open('attack.txt', 'r') as afile2:
            buf = afile2.read()
        b = prehash(buf)
       
        if (a==b):
                collision = 1
                print("Collision found on try", i,"with hex digit",b)
        else:
                if ((i%1000)==0):
                        print(i)
                i += 1
                afile2.close()
                
