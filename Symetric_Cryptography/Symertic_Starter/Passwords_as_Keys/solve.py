from Crypto.Cipher import AES
from hashlib import md5
import requests, json

r = requests.get('https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words')
lst = r.content.decode().split('\n')
# print(data.split('\n'))
r = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
data = json.loads(r.content.decode())
ct = bytes.fromhex(data['ciphertext'])


for i in lst:
    key = md5(i.strip().encode()).digest()
    # print(key)
    cipher = AES.new(key, AES.MODE_ECB)
    data = cipher.decrypt(ct)
    if b'crypto' in data:
        print("FOUND: {}".format(data))
        break