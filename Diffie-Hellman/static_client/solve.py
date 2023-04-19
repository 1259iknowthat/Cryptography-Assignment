from pwn import *
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from sympy.ntheory import discrete_log
from math import prod
from Crypto.Util.number import *
from random import randint

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    #print(key)
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


def genSmoothPrime(bitlen):
	p = 2
	ls = [2]
	while p.bit_length() < bitlen:
		q = getPrime(20)
		p *= q
		ls.append(q)
	while True:
		q = getPrime(20)
		if isPrime(p*q + 1):
	    		p = p*q
	    		ls.append(q)
	    		break
	return (p + 1), ls



  
host, port = "socket.cryptohack.org" , 13373
client=remote(host,port)

"""
client.recvuntil("Intercepted from Alice: ")
data=json.loads(client.recvline())
A=int(data['A'],16)
p=int(data['p'],16)

client.recvuntil("Intercepted from Alice: ")
data=json.loads(client.recvline())
print(data)
flag_enc=data['encrypted']
flag_iv=data['iv']


client.recvuntil("Bob connects to you, send him some parameters: ")
data={}
cus_p, cus_p_factors=genSmoothPrime(1700)
cus_g=2
a=randint(2,cus_p-1)
cus_A=pow(cus_g,a,cus_p)
data['p']=hex(cus_p)
data['g']=hex(cus_g)
data['A']=hex(cus_A)



client.sendline(json.dumps(data))
#client.interactive()

client.recvuntil("Bob says to you: ")
data=json.loads(client.recvline())


b=discrete_log(cus_p,int(data['B'],16),cus_g)
print(f"This is fixed b {b}")#fixed B

#b=7273086812095034626784775786097754621334165238025575189513823623757449151828989133272386733165672487334918104579752730239236482456859355299966043051967152355891722647737316132882736754216386588471521625488245492658778640563255153908640240666465936742010092343138819760416990263824784017585372945862055710962051722860071532575482978715347226585309392243879335202050749293111270413003966719322119397363604669588801595943715334918202175411011553013930826415773226

client.recvuntil("Bob says to you: ")
data=json.loads(client.recvline())
shared_secret = pow(cus_A,b,cus_p)
iv = data['iv']
ciphertext = data['encrypted']
print(decrypt_flag(shared_secret,iv,ciphertext))


flag_shared_secret = pow(A,b,p)
iv = flag_iv
ciphertext = flag_enc
print(decrypt_flag(flag_shared_secret,iv,ciphertext))
client.interactive()
"""
client.recvuntil("Intercepted from Alice: ")
data=json.loads(client.recvline())
A=int(data['A'],16)
p=int(data['p'],16)
g=int(data['g'],16)

client.recvuntil("Intercepted from Alice: ")
data=json.loads(client.recvline())
print(data)
flag_enc=data['encrypted']
flag_iv=data['iv']

client.recvuntil("Bob connects to you, send him some parameters: ")
data={}
data['p']=hex(p)
data['g']=hex(A)
data['A']=hex(3)
client.sendline(json.dumps(data))


client.recvuntil("Bob says to you: ")
data=json.loads(client.recvline())
print(data)


shared_secret=int(data['B'],16)
print(shared_secret)
#shared_secret = pow(cus_A,b,cus_p)
iv=flag_iv
ciphertext=flag_enc
print(decrypt_flag(shared_secret,iv,ciphertext))

