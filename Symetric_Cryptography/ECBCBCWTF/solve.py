from Crypto.Cipher import AES
from pwn import *
import requests
import json

r1 = requests.get('https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/')
data = json.loads(r1.content.decode())
# print(data['ciphertext'])
ct = bytes.fromhex(data['ciphertext'])

r2 = requests.get('https://aes.cryptohack.org/ecbcbcwtf/decrypt/{}/'.format(ct.hex()))

data = json.loads(r2.content.decode())
# print(data)
pt = bytes.fromhex(data['plaintext'])

iv = ct[:16]
ct1 = ct[16:32]
# ct2 = ct[32:]
pt1 = pt[16:32]
pt2 = pt[32:]
# print(len(pt1), len(pt2))
# print(len(ct1))
# print(len(iv))
data1 = xor(iv, pt1)
data2 = xor(ct1, pt2)
print(data1+data2)
