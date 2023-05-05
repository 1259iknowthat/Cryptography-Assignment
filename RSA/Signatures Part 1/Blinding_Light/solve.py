#This code is contributed by tranminhprvt01
from pwn import *
import json
import random
from Crypto.Util.number import bytes_to_long, long_to_bytes

host, port = "socket.cryptohack.org", 13376

r=remote(host,port)

r.recvuntil("Watch out for the Blinding Light\n")

data={}
data['option'] = "get_pubkey"
r.sendline(json.dumps(data))

data=json.loads(r.recvline())

n=int(data['N'], 16)
e=int(data['e'], 16)


print(n)
print(e)

#Blinding attack

#choosing random r
randval=2
print("random value",randval)
ADMIN_TOKEN = b"admin=True" #M
fake_m = (pow(randval,e,n)*bytes_to_long(ADMIN_TOKEN)) % n
print("fake_m",fake_m)
print(hex(fake_m))

#sign fake m
data={}
data['option'] = "sign"
data['msg'] = long_to_bytes(fake_m).hex()
r.sendline(json.dumps(data))

data=json.loads(r.recvline())
print(data)

fake_msg=data['msg']
fake_sign=int(data['signature'], 16)


real_sign = (fake_sign // randval) % n


#verify
data={}
data['option'] = "verify"
data['msg'] = ADMIN_TOKEN.hex()
data['signature'] = hex(real_sign)
data=json.dumps(data)
r.sendline(data)

data=json.loads(r.recvline())
print(data)





