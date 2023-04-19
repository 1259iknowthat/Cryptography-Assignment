def xor(a,b):
	a=bytes.fromhex(a)
	b=bytes.fromhex(b)
	return ''.join(list(chr(i^j) for i, j in zip(a,b)))
import requests

base_url="https://aes.cryptohack.org"

r=requests.get(f"{base_url}/ecbcbcwtf/encrypt_flag")
data=r.json()
ct=data["ciphertext"]
iv=ct[:32] #len iv = 16
enc=ct[32:]
print(ct)
print(iv)
print(enc,len(enc))

flag=""

#lam nguoc (tu phai qua trai)
k=len(enc)//32
tmp=enc[32*(k-1):32*k]
print(tmp,len(tmp))
while (k > 1):
	prev=enc[32*(k-2):32*(k-1)]
	r=requests.get(f"{base_url}/ecbcbcwtf/decrypt/{tmp}")
	data=r.json()
	#print(data)
	pt1=data["plaintext"]
	flag=xor(pt1,prev)+flag
	k-=1
	tmp=prev
#print(flag)
prev=iv
r=requests.get(f"{base_url}/ecbcbcwtf/decrypt/{tmp}")
data=r.json()
print(data)
pt1=data["plaintext"]
flag=xor(pt1,prev)+flag
print(flag)

"""
#lam xuoi (tu trai qua phai)
k=len(enc)//32
tmp=enc[:32]
r=requests.get(f"{base_url}/ecbcbcwtf/decrypt/{tmp}")
data=r.json()
pt1=data["plaintext"]
flag=flag+xor(pt1,iv)
for i in range(1,k):
	current_iv=tmp
	tmp=enc[32*i:32*(i+1)]
	r=requests.get(f"{base_url}/ecbcbcwtf/decrypt/{tmp}")
	data=r.json()
	pt1=data["plaintext"]
	flag=flag+xor(pt1,current_iv)
print(flag)
"""
