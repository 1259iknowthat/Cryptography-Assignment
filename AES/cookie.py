from pwn import *

ct =  bytes.fromhex("72c905b67a2edcc2a6b7d49e6ab7259f483593ebfd98f18dd80363c1777aef093b69c5740667cf1986d5d3ded1ec109b")
pt1 = b'admin=False;expi'
iv = ct[:16]
cookie = ct[16:]

print(iv.hex(), len(iv))
print(cookie.hex(), len(cookie))
# print(pt1.decode())
block = xor(pt1, iv)
print(block.hex(), len(block))

fake_cookie = b'admin=True;;expi'
iv_fake = xor(block, fake_cookie)
print(iv_fake, len(iv_fake))
# check if iv was good
new_cred = xor((iv_fake), block)
print(new_cred)