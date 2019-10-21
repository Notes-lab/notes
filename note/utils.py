# import base64
#
#
# def encode(key, clear):
#     enc = []
#     for i in range(len(clear)):
#         key_c = key[i % len(key)]
#         enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
#         enc.append(enc_c)
#     return base64.urlsafe_b64encode("".join(enc).encode()).decode()
#
#
# def decode(key, enc):
#     dec = []
#     enc = base64.urlsafe_b64decode(enc).decode()
#     for i in range(len(enc)):
#         key_c = key[i % len(key)]
#         dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
#         dec.append(dec_c)
#     return "".join(dec)

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(plaintext, password):
    f = Fernet(base64.urlsafe_b64encode(PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b'abcd', iterations=1000, backend=default_backend()).derive(password.encode())))
    return f.encrypt(plaintext.encode()).decode()

def decrypt(ciphertext, password):
    f = Fernet(base64.urlsafe_b64encode(PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b'abcd', iterations=1000, backend=default_backend()).derive(password.encode())))
    return f.decrypt(ciphertext.encode()).decode()
