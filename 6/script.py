import hashlib
import sys

def getHash(message):
    salt = "Km5d5ivMy8iexuHcZrsD"
    dk = hashlib.pbkdf2_hmac('sha512', message.encode(), salt.encode(), 200000)
    return dk.hex()

if(len(sys.argv) != 2):
    print('Usage: python3 script.py STRING_TO_BE_HASHED')
else: 
    print(f'PBKDF2 hash value of [{sys.argv[1]}]:')
    print(getHash(sys.argv[1]))
