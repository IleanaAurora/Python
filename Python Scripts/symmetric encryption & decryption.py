#Prerequisites:
    #first ensure you have the cryptography module by going to cmd prompt and
        #typing 'pip install cryptography'
    #have a .csv file to encrypt in the same file dir as this program
#Note: Fernet is an implementation of symmetric aka secret key authenticated
    #cryptography & guarantees that a message encrypted using it cannot be
    #manipulated or read without the key
#Algorithm:
    #import the crytography module & fernet
    #generate a key
    #save the key to the file system
    #get the key from the file system
    #open & read the file to encrypt
    #write and save the encrypted file to a new file in the file system
    #open & read the file to decrypt
    #write and save the decrypted file to a new file in the file system


import cryptography
from cryptography.fernet import Fernet

sampleFile = 'sampleFile.csv'
encSampleFile = 'sampleFile.csv.encrypted'
decSampleFile = 'sampleFile.csv.decrypted'

myKey = Fernet.generate_key()
print("The following key was generated:",myKey)

file = open('myKey.key', 'wb') #wb means write bytes
file.write(myKey)
file.close()

file = open('myKey.key', 'rb') # rb means read bytes
myKey  = file.read()
file.close()

with open(sampleFile, 'rb') as f:
    data = f.read()
print("\nThe original file contents read",data)
fernet = Fernet(myKey)
encrypted = fernet.encrypt(data)

with open(encSampleFile, 'wb') as f:
    f.write(encrypted)

with open(encSampleFile, 'rb') as f:
    data = f.read()
print("\nThe encrypted file contents read",data)
decrypted = fernet.decrypt(data)

with open(decSampleFile, 'wb') as f:
    f.write(decrypted)

with open(decSampleFile, 'rb') as f:
    data = f.read()
print("\nThe decrypted file contents read",data)
