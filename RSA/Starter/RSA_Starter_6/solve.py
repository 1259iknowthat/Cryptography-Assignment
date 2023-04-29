import hashlib
from Crypto.Util.number import *
f=open("private.key",'r')
data=f.readlines()
cnt=0
for i in data:
	if cnt == 0: N=int(i[4:-1])
	else: d=int(i[4:-1])
	cnt+=1
print(N)
print(d)
m=b"crypto{Immut4ble_m3ssag1ng}"

hash_m=hashlib.sha256(m).digest()
print(hash_m)
sign_message=long_to_bytes(pow(bytes_to_long(hash_m),d,N))
print(sign_message.hex())
