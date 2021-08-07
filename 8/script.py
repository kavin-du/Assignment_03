import hashlib
import sys, os

def getHash(message):
    salt = os.urandom(16) # 16 bytes secure random
    return hashlib.sha512(salt + message.encode()).hexdigest()

if(len(sys.argv) != 2):
    print('Usage: python3 script.py STRING_TO_BE_HASHED')
else: 
    print(f'SHA512 hash value of [{sys.argv[1]}] using random value as salt:')
    print(getHash(sys.argv[1]))
