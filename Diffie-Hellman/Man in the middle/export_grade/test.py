import math as mt
from sympy.ntheory import discrete_log
from pwn import remote
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from Crypto.Util.number import inverse

factors={}
def factorization(p):
	i=2
	while (i <= mt.sqrt(p)):
		if (p % i == 0): 
			cnt=0
			#print(i)
			while (p % i == 0):
				cnt+=1
				p//=i
			factors[i]=cnt
		i+=1
	if (p != 1): factors[p]=1
	
def xMod(y, g, p, pi, cnt):
	res=0
	#print(pi, cnt, y)
	for i in range(cnt):
		#print(y)
		Y=pow(y, (p-1)//pow(pi, i+1,p), p)
		G=pow(g, (p-1)//pi, p)
		print(Y, G, pi, i)
		F=discrete_log(p, Y, g)
		#print(F)
		F=F//((p-1)//(pi)) 
		print(F)
		res+=pow(pi, i, p) * F 
		y=y * pow(g, -F, p) % p
	return res % pow(pi, cnt) 
	
def CRT(a,n):
	l=len(a)
	N=mt.prod(n)
	Ni=[mt.prod(n[:i])*mt.prod(n[i+1:]) for i in range(l)]
	y=[inverse(Ni[i],n[i]) for i in range(l)]
	
	res=0
	for i in range(l):
		res+=a[i]*Ni[i]*y[i]
	res%=N
	return res

def PH(y, g, p):
	#factorize p-1
	factorization(p-1)
	#print(factors)
	xi=[]
	pi=[]
	for i in factors:
		xi.append(xMod(y, g, p, i, factors[i]))
		pi.append(i**factors[i])
	print(xi,pi)
	return CRT(xi,pi)

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    print(key)
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    

ip="socket.cryptohack.org"
port= 13379

client=remote(ip,port)

#access Alice's message and modify and send to Bob
client.recvuntil("Intercepted from Alice: ")
data=json.loads(client.recvline())
data['supported']=["DH64"]
client.recvuntil("Send to Bob: ")
client.sendline(json.dumps(data))

#access Bob's message and send to Alice
client.recvuntil("Intercepted from Bob: ")
data=client.recvline()
client.recvuntil("Send to Alice: ")
client.sendline(data)

client.recvuntil("Intercepted from Alice: ")
data=json.loads(client.recvline())
p=int(data['p'],16)
g=int(data['g'],16)
A=int(data['A'],16)
client.recvuntil("Intercepted from Bob: ")
data=json.loads(client.recvline())
B=int(data['B'],16)
client.recvuntil("Intercepted from Alice: ")
data=json.loads(client.recvline())
iv=data['iv']
enc=data['encrypted_flag']


print(p,g,A,B)
print(iv,enc)

a=PH(A, g, p)
b=PH(B, g, p)

shared_secret=pow(A,b,p)
tmp=pow(B,a,p)

print(shared_secret==tmp) #2 thang nay bang nhau thi dung hmm tai vi hom qua tui test doan nay thi 
# no bang nhau


print(decrypt_flag(shared_secret, iv, enc))


#print(PH(7531, 6, 8101)) 


