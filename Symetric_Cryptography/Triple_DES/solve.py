import requests
import json
from binascii import hexlify, unhexlify
import string

alphabet=string.ascii_letters
"""
base_url="https://aes.cryptohack.org/triple_des/"
key="1234567887654321"
key=hexlify(key.encode()).decode()
r=requests.get(f"{base_url}/encrypt_flag/{key}")
recv=r.json()
print(recv)
ct=recv['ciphertext']
print(ct,len(ct))

blocks=[ct[i:i+16] for i in range(0,len(ct),16)]

print(blocks)

known="crypto{"
for i in alphabet:
	tmp=known
	tmp+=i
	print(tmp,i)
	data=hexlify(tmp.encode()).decode()
	r=requests.get(f"{base_url}/encrypt/{key}/{data}")
	recv=r.json()
	if recv['ciphertext'] == blocks[0]:
		print(recv,i)
		break
	print(recv)
"""
from Crypto.Cipher import DES3

def xor(a, b):
	# xor 2 bytestrings, repeating the 2nd one if necessary
	return bytes(x ^ y for x,y in zip(a, b * (1 + len(a) // len(b))))


key="31323334353637383837363534333231"
flag="63727970746f7b6e"
iv=b"a8byteiv"
key=bytes.fromhex(key)
pt=bytes.fromhex(flag)
pt=xor(pt,iv)
cipher=DES3.new(key, DES3.MODE_ECB)
ct=cipher.encrypt(pt)
ct=xor(ct,iv)
print(ct,ct.hex())
s=ct.hex()
print(iv,len(iv))

"""
3DES split key in two halves K1 || K2 or 3 part K1 || K2 || K3
so we need all of them to be weak key and combine
becuz weak key cause DES encrypt twice become itself DES(key,DES(key,p))=p
"""
s=bytes.fromhex(s)
s=xor(s,iv)
print("1",s)
s=cipher.encrypt(s)
print("2",s)
s=xor(s,iv)
print("3",s)



