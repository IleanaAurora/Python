import math
import hashlib
import os

hash_byte_size = 2

BLOCKSIZE = 65536
hasher = hashlib.shake_256()
with open('attack.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)

a = hasher.hexdigest(hash_byte_size)
print(a)

collision = 0
characters = 0
file1 = open('noattack.txt', 'r')

for line in file1:
        characters = characters + len(line)

file1.close()
file1 = open('noattack.txt', 'a')
file1.seek(characters,0)
bin_0 = format(0, '064b')
print(bin_0)
file1.write(bin_0)
file1.close()

max = pow(2, 64)

i = 0

while (i<max) & (collision == 0):
        with open('noattack.txt', 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        b = hasher.hexdigest(hash_byte_size)
       
        if (a==b):
                collision = 1
                print("COLLISION", i, b)
        else:
                if ((i%1000)==0):
                        print(i)
                i = i+1
                afile.close()
                afile = open('noattack.txt', 'a')
                afile.seek(characters,0)
                afile.truncate()
                bin_i = format(i, '064b')
                afile.write(bin_i)
                afile.close()
                
