import os, binascii
from backports.pbkdf2 import pbkdf2_hmac, compare_digest

password = b"super secret password"
salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')

hashed = pbkdf2_hmac("sha256", password, salt, 50000)

print(binascii.hexlify(hashed))
print(hashed)
# if compare_digest(password, hashed):
#     print("It Matches!")
# else:
#     print("It Does not Match :(")
