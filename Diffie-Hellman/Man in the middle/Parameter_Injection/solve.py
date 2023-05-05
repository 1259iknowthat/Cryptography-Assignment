#This code is contributed by tranminhprvt01
from pwn import remote
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


ip="socket.cryptohack.org"
port= 13371




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


client=remote(ip,port)
#access Alice's message and send to Bob
client.recvuntil("Intercepted from Alice: ")
data=client.recvline()
client.recvuntil("Send to Bob: ")
client.send(data)

#modify Bob's message and send to Alice
client.recvuntil("Intercepted from Bob: ")
data=json.loads(client.recvline())
data['B']="1"
client.recvuntil("Send to Alice: ")
client.sendline(json.dumps(data))

#get iv and encrypted_flag from Alice
client.recvuntil("Intercepted from Alice: ")
data=json.loads(client.recvline())


shared_secret=1
iv=data['iv']
encrypted_flag=data['encrypted_flag']

print(iv,encrypted_flag)
print(decrypt_flag(shared_secret, iv, encrypted_flag))




