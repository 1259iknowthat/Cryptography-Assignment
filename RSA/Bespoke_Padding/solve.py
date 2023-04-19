import socket
import json
from Crypto.Util.number import long_to_bytes

e = 11

ct = []
pads = []
N = None
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("socket.cryptohack.org", 13386))
    s.recv(1024)
    for i in range(2):
        s.sendall(b'{"option":"get_flag"}')
        # the response may be longer than one packet, so make sure we get all of it
        data = b""
        while not data.endswith(b'\n'):
            data += s.recv(1024)
        data = json.loads(data)
        ct.append(data['encrypted_flag'])
        pads.append(data['padding'])
        N = data['modulus']

def gcd(a,b):
    # custom GCD implementation because Sage's one apparently doesn't work here
    while b:
        a, b = b, a % b
    return a.monic()

P.<x> = PolynomialRing(Zmod(N))
p1 = (pads[0][0] * x + pads[0][1]) ^ e - ct[0]
p2 = (pads[1][0] * x + pads[1][1]) ^ e - ct[1]
result = -gcd(p1, p2).coefficients()[0]
print(long_to_bytes(result))
