import requests

weak_key = '0101010101010101FEFEFEFEFEFEFEFE'

r = requests.get(url='https://aes.cryptohack.org/triple_des/encrypt_flag/{}'.format(weak_key))
# print(r.json())
ct = r.json()
print(ct['ciphertext'])
ct = ct['ciphertext']

r = requests.get(url='https://aes.cryptohack.org/triple_des/encrypt/{}/{}'.format(weak_key, ct))
# print(r)
pt = r.json()
print(pt['ciphertext'])
pt = pt['ciphertext']
print(bytes.fromhex(pt))