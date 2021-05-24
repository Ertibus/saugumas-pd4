import hashlib
import os

class PBKDF2Hasher:
    @classmethod
    def encrypt(self, password:str, salt = b'0'):
        if salt == b'0':
            salt = os.urandom(32)
        else:
            salt = bytes.fromhex(salt)

        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        return salt.hex(), key.hex();
        

