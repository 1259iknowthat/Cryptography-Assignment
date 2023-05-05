#This code is contributed by tranminhprvt01
from pwn import remote
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import math as mt
from sympy.ntheory import discrete_log


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
    
    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

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
"""
def CRT(a,n):
	l=len(a)
	N=mt.prod(n)
	Ni=[mt.prod(n[:i])*mt.prod(n[i+1:]) for i in range(l)]
	y=[pow(Ni[i],-1,n[i]) for i in range(l)]
	
	res=0
	for i in range(l):
		res+=a[i]*Ni[i]*y[i]
	res%=N
	return res
#https://cp-algorithms.com/algebra/discrete-log.html#algorithm
def bsgs(a, b, m):
	a%=m
	b%=m
	n=mt.trunc(mt.sqrt(m))+1
	vals={}
	#print(n,len(str(n)))
	for p in range(1,n+1):
		vals[pow(a,p*n,m)]=p
	#print(vals)
	for q in range(n+1):
		cur=(pow(a,q,m)*b)%m
		#print(cur)
		if (cur in vals):
			ans=vals[cur]*n-q
			return ans
	return -1
#https://risencrypto.github.io/PohligHellman/
def PH(g, A, p):
	p_order=[2, 3, 293, 5417, 420233272499]
	powers=[3, 1, 1, 1, 1]
	#p_order=[2, 3, 5]
	#powers=[2, 4, 2]
	pi=[(i**j) for i, j in zip(p_order,powers)]
	xi=[]
	for i, j in zip(p_order,powers):
		res=0
		for k in range(j):
			mu=(p-1)//(i**(k+1)) # ->
			print(mu,mu*(i**k))
			lhs=pow(A*(pow(g,-res,p)), mu, p)
			#tmp=bsgs(g, lhs, p)//(mu*(i**k)) 
			tmp=discrete_log(p,lhs,g)//((p-1)//i)
			v
			#if lhs==1: tmp=0
			res+=(i**k)*(tmp)
			print(i,j,k,mu,lhs,tmp)
		xi.append(res)
	print(xi)
	print(pi)		
	
	#CRT to combine to solve for x
	return CRT(xi,pi)
	
#16007670376277647657
#g^a = A (mod p) -> compute a using PH algorithm


# 15934426402070882847 

p=16007670376277647657
g=2
A=7576263658413204236
B=8358626865267287946
iv="cd57b3eedc0d4cb50cd79f7087964aad"
enc="e9fb1df607fddc92f3b47d319198d6bcb1e2ea344e974452114f9fab61585ee7"

a=PH(g,A,p)
#print(a)
shared_secret=pow(B,a,p)
b=PH(g,B,p)
#print(b)
tmp=pow(A,b,p)
print(tmp==shared_secret)

print(decrypt_flag(shared_secret, iv, enc))
"""
a=discrete_log(p,A,g)
print(a)
print(pow(g,a,p) == A)
b=discrete_log(p,B,g)
shared_secret=pow(B,a,p)
tmp=pow(A,b,p)
print(shared_secret == tmp)
print(decrypt_flag(shared_secret, iv, enc))
