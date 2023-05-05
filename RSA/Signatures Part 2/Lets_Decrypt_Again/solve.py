#This code is contributed by tranminhprvt01
from pwn import *
import json
import hashlib
import re
import secrets
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime, inverse, isPrime
from pythonpkcs1.pkcs1 import emsa_pkcs1_v15

host, port = "socket.cryptohack.org", 13394

r=remote(host,port)

r.recvuntil("This server validates statements we make for you. Present your messages and public key, and if the signature matches ours, you must undoubtably be us. Just do it multiple times to make sure...\n")


data={}
data['option'] = "get_signature"
r.sendline(json.dumps(data))

data=json.loads(r.recvline())

N=int(data['N'], 16)
E=int(data['E'], 16)
sign=int(data['signature'], 16)


print(N)
print(E)
print(sign)



def xor(a, b):
    assert len(a) == len(b)
    return bytes(x ^ y for x, y in zip(a, b))


def btc_check(msg):
    alpha = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    addr = BTC_PAT.match(msg)
    if not addr:
        return False
    addr = addr.group(1)
    raw = b"\0" * (len(addr) - len(addr.lstrip(alpha[0])))
    res = 0
    for c in addr:
        res *= 58
        res += alpha.index(c)
    raw += long_to_bytes(res)

    if len(raw) != 25:
        return False
    if raw[0] not in [0, 5]:
        return False
    return raw[-4:] == hashlib.sha256(hashlib.sha256(raw[:-4]).digest()).digest()[:4]


PATTERNS = [
    re.compile(r"^This is a test(.*)for a fake signature.$").match,
    re.compile(r"^My name is ([a-zA-Z\s]+) and I own CryptoHack.org$").match,
    btc_check
]



FLAG = b"abcdefgh"

D=5

BIT_LENGTH = 768

MSG = b'We are hyperreality and Jack and we own CryptoHack.org'
DIGEST = emsa_pkcs1_v15.encode(MSG, BIT_LENGTH // 8)
SIGNATURE = pow(bytes_to_long(DIGEST), D, N)
BTC_PAT = re.compile("^Please send all my money to ([1-9A-HJ-NP-Za-km-z]+)$")



print(btc_check("abc"))



