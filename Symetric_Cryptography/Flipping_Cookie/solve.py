from binascii import *
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
cookie = f"admin=False;expiry={expires_at}".encode()
padded = pad(cookie, 16)
print(cookie,len(cookie))
print(padded,len(padded))

import requests

base_url="http://aes.cryptohack.org/flipping_cookie/"

r=requests.get(f"{base_url}get_cookie")
data=r.json()
ct=data["cookie"]
iv=ct[:32]
enc=ct[32:]
print(ct)
print(iv)
print(enc)
print(3^2^2)
fake_cookie=b"admin=True;expiry=000000"

tmp=iv
tmp=bytes.fromhex(tmp)
ls=[tmp[i] for i in range(16)]
print(ls)
for i in range(16):
	ls[i]=ls[i]^cookie[i]^fake_cookie[i]
print(ls)
custom_iv=bytes(ls)
custom_iv=custom_iv.hex()
r=requests.get(f"{base_url}check_admin/{enc}/{custom_iv}")
data=r.json()
print(data)

