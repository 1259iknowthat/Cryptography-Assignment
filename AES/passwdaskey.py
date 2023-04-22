from Crypto.Cipher import AES
from hashlib import md5

ct = bytes.fromhex("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66")
with open("dict", 'r') as f:
    for i in f.readlines():
        key = md5(i.strip().encode()).digest()
        # print(key)
        cipher = AES.new(key, AES.MODE_ECB)
        data = cipher.decrypt(ct)
        if b'crypto' in data:
            print("FOUND: {}".format(data))
            break