#This code is contributed by tranminhprvt01
from Crypto.Util.number import long_to_bytes
from pwn import *
import json

import re
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes
#from utils import listener
from pythonpkcs1.pkcs1 import emsa_pkcs1_v15
#from pkcs1 import emsa_pkcs1_v15


host, port = "socket.cryptohack.org", 13391

r=remote(host,port)

r.recvuntil("This server validates domain ownership with RSA signatures. Present your message and public key, and if the signature matches ours, you must own the domain.\n")

data={}
data['option'] = "get_signature"
r.sendline(json.dumps(data))

data=json.loads(r.recvline())

n=int(data['N'], 16)
e=int(data['e'], 16)
sign=int(data['signature'], 16)

print(n)
print(e)
print(sign)

MSG = 'We are hyperreality and Jack and we own CryptoHack.org'
DIGEST = emsa_pkcs1_v15.encode(MSG.encode(), 256)
SIGNATURE = sign
print(bytes_to_long(DIGEST))


base_msg = "I am Mallory and I own CryptoHack.org"

msg=base_msg
digest = emsa_pkcs1_v15.encode(msg.encode(), 256)
n=sign-bytes_to_long(digest)
print(n)

data={}
data['option'] = "verify"
data['msg'] = msg
data['N'] = hex(n)
data['e'] = hex(1)

data=json.dumps(data)

r.sendline(data)
print(r.recv())







