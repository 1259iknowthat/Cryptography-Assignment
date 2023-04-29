import requests
from binascii import unhexlify
base_url="http://aes.cryptohack.org/symmetry"

r=requests.get(f"{base_url}/encrypt_flag")
data=r.json()["ciphertext"]
print(data)
iv=data[:32]
ct=data[32:]
print(iv)
print(ct)


pt=ct
r=requests.get(f"{base_url}/encrypt/{pt}/{iv}")
data=r.json()["ciphertext"]
print(unhexlify(data))
