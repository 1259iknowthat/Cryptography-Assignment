#This code is contributed by tranminhprvt01
from Crypto.Util.number import long_to_bytes
from pwn import remote
import json

host, port = "socket.cryptohack.org", 13374

r=remote(host,port)

r.recvuntil("Welcome to my signing server. You can get_pubkey, get_secret, or sign.\n")

data={}
data['option'] = "get_pubkey"
r.sendline(json.dumps(data))

data=json.loads(r.recvline())

n=int(data['N'], 16)
e=int(data['e'], 16)

print(n)
print(e)

data={}
data['option'] = "get_secret"
r.sendline(json.dumps(data))

data=json.loads(r.recvline())
c=int(data['secret'], 16)

print(c)

data={}
data['option'] = "sign"
data['msg'] = hex(c)
r.sendline(json.dumps(data))

data=json.loads(r.recvline())

m=int(data['signature'], 16)

print(long_to_bytes(m))


