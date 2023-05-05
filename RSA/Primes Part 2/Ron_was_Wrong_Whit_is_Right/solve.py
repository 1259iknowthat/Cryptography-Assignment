#This code is contributed by tranminhprvt01
import os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from math import gcd
from Crypto.Util.number import inverse

dirs=os.listdir("./keys_and_messages")
cnt=0
modulus=[]
for file_ in dirs:
	if file_.endswith(".pem"):
		cnt+=1
		key=RSA.importKey(open("./keys_and_messages/{}.pem".format(cnt),'r').read())
		print(cnt)
		modulus.append(key.n)
		print(key.n, key.e)


n=modulus[20] #21.pub
e=0x10001

res=[]
for i in modulus:
	if i != n and gcd(i,n) != 1: res.append((i,gcd(i,n)))
print(res, len(res))


p=res[0][1]
q=n//p
phi=(p-1)*(q-1)
d=inverse(e,phi)

enc=open("./keys_and_messages/21.ciphertext",'r').read()
enc=bytes.fromhex(enc)

key=RSA.construct((n, e, d))
cipher=PKCS1_OAEP.new(key)
FLAG=cipher.decrypt(enc)

print(FLAG)


