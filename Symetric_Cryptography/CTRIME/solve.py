import requests
import json
import string

alphabet=string.ascii_letters
alphabet+="_}{1234567890"
print(alphabet)

base_url = "http://aes.cryptohack.org/ctrime"

data=b"crypto{CRIME"
r=requests.get(f"{base_url}/encrypt/{data.hex()}")
recv=r.json()
print(recv)
ct=recv["ciphertext"]
print(ct,len(ct))
tmp=len(ct)

while True:
	for i in alphabet:
		tries=data+i.encode()
		r=requests.get(f"{base_url}/encrypt/{tries.hex()}")
		recv=r.json()
		ct=recv["ciphertext"]
		print(i,ct,tries)
		print(len(ct),tmp)
		if len(ct) == tmp:
			tmp=len(ct)
			data=tries
			break
	if data[-1] == b"}" : break



