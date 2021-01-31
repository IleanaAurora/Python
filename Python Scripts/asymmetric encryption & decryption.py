#Prerequisites:
    #first ensure you have the cryptography module by going to cmd prompt and
        #typing 'pip install cryptography'
    #have a .csv file to encrypt in the same file dir as this program
#Note: we will be using rsa encryption
#Algorithm:
    #import the crytography module & hazmat functionalities for rsa encrption
    #generate public & private keys
    #serialize the keys before saving them to the file system
    #store the keys in the file system
    #read the keys back in
    #open & read the file to encrypt
    #write and save the encrypted file to a new file in the file system
    #open & read the file to decrypt
    #write and save the decrypted file to a new file in the file system

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


privateKey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
publicKey = privateKey.public_key()

print("The following private key was generated:",privateKey)
print("\nThe following public key was generated:",publicKey)

pem = privateKey.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
with open('privateKey.pem', 'wb') as f:
    f.write(pem)

pem = publicKey.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
with open('publicKey.pem', 'wb') as f:
    f.write(pem)



with open("privateKey.pem", "rb") as key_file:
        privateKey = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
with open("publicKey.pem", "rb") as key_file:
        publicKey = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )



f = open('sampleFile.csv', 'rb')
data = f.read()
f.close()
print("\nThe original file contents read",data)

        
encrypted = publicKey.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

f = open('sampleFile.RSAencrypted', 'wb')
f.write(encrypted)
f.close()
print("\nThe encrypted file contents read",encrypted)

decrypted = privateKey.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

f = open('sampleFile.RSAdecrypted', 'wb')
f.write(decrypted)
f.close()
print("\nThe decrypted file contents read",decrypted)
