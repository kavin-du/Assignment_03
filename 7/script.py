import hashlib
import sys, os

def getHash(message):
    salt = os.urandom(16) # 16 bytes secure random
    dk = hashlib.pbkdf2_hmac('sha512', message.encode(), salt, 200000)
    return dk.hex()

if(len(sys.argv) != 2):
    print('Usage: python3 script.py STRING_TO_BE_HASHED')
else: 
    print(f'PBKDF2 hash value of [{sys.argv[1]}] using random value as salt:')
    print(getHash(sys.argv[1]))
