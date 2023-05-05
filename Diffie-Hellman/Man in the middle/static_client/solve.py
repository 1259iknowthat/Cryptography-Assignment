#This code is contributed by tranminhprvt01
from pwn import *
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from sympy.ntheory import discrete_log
from math import prod
from Crypto.Util.number import *
from random import randint
import time

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

  
host, port = "socket.cryptohack.org" , 13373

#This part for decrypt message between us and Bob
client=remote(host,port)
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

cus_p = 17
cus_g = 2
cus_A = 2

client.recvuntil("Bob connects to you, send him some parameters: ")
data={}
data['p']=hex(cus_p)
data['g']=hex(cus_g)
data['A']=hex(cus_A)
print(data)
client.sendline(json.dumps(data))


client.recvuntil("Bob says to you: ")
data=json.loads(client.recvline())
print(data)


B=int(data['B'],16)
b=discrete_log(cus_p, B, cus_g)
print("Found secret exponent b =",b)

client.recvuntil("Bob says to you: ")
data=json.loads(client.recvline())
shared_secret = pow(cus_A,b,cus_p)
iv = data['iv']
ciphertext = data['encrypted']
print(decrypt_flag(shared_secret,iv,ciphertext))
client.close()

sleep(5)

#This part is for decrypting message between Alice and Bob
client=remote(host,port)
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
print(data)
client.sendline(json.dumps(data))


client.recvuntil("Bob says to you: ")
data=json.loads(client.recvline())
print(data)


shared_secret=int(data['B'],16)
print(shared_secret)
iv=flag_iv
ciphertext=flag_enc
print(decrypt_flag(shared_secret,iv,ciphertext))
