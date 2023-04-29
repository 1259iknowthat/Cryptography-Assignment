from pwn import *
import requests
import json


# ct =  bytes.fromhex("72c905b67a2edcc2a6b7d49e6ab7259f483593ebfd98f18dd80363c1777aef093b69c5740667cf1986d5d3ded1ec109b")

r = requests.get('https://aes.cryptohack.org/flipping_cookie/get_cookie/')
data = json.loads(r.content.decode())
ct = bytes.fromhex(data['cookie'])

pt1 = b'admin=False;expi'
iv = ct[:16]
cookie = ct[16:]

# print(iv.hex(), len(iv))
# print(cookie.hex(), len(cookie))
# print(pt1.decode())
block = xor(pt1, iv)
# print(block.hex(), len(block))

fake_cookie = b'admin=True;;expi'
iv_fake = xor(block, fake_cookie)
# print(iv_fake, len(iv_fake))
iv_fake = iv_fake.hex()
# print(iv_fake, fake_cookie)
r = requests.get('https://aes.cryptohack.org/flipping_cookie/check_admin/{}/{}/'.format(cookie.hex(), iv_fake))

print(r.content)
