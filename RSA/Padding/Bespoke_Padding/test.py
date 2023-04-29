from pwn import *

host, port = "socket.cryptohack.org", 13386

c = remote(host, port)

data=c.recvuntil("want")

print(c.recv())

print(data)


