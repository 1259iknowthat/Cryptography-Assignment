from pwn import *
import requests, json


pt = bytes.fromhex('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
r = requests.get('https://aes.cryptohack.org/lazy_cbc/encrypt/{}'.format(pt.hex()))
data = json.loads(r.content.decode())
ct = data['ciphertext']

ct = bytes.fromhex(ct)

ct1 = ct[:16]

tmp_ct3 = ct1[:]
tmp_ct2 = b'\x00' * 16
tmp_ct = ct1 + tmp_ct2 + tmp_ct3
# print(tmp_ct.hex())

r = requests.get('https://aes.cryptohack.org/lazy_cbc/receive/{}'.format(tmp_ct.hex()))
data = json.loads(r.content.decode())
invalid_pt = data['error']
# print(invalid_pt[19:])

invalid_pt = bytes.fromhex(invalid_pt[19:])
key = xor(invalid_pt[:16], invalid_pt[32:])
# print(key, key.hex())

r = requests.get('https://aes.cryptohack.org/lazy_cbc/get_flag/{}'.format(key.hex()))
data = json.loads(r.content.decode())
print(bytes.fromhex(data['plaintext']))