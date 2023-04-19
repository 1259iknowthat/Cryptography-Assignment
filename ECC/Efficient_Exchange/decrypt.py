from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

"""
ECC format
y^2=x^3 + ax + b (mod p)
"""

a=497
b=1768
p=9739
O=(0,0)
def cal(x):
	return x*x*x+a*x+b 
def add(p, q, MOD):
	if p == O: return q
	elif q == O: return p
	else:
		x1=p[0]
		y1=p[1]
		x2=q[0]
		y2=q[1]
		if x1 == x2 and y1 == -y2: return O
		else:
			if p != q: 
				lamda=(y2-y1)*pow(x2-x1,-1,MOD)
			else: lamda=(3*x1*x1 + a)*pow(2*y1,-1,MOD)
		x3=lamda*lamda-x1-x2
		y3=lamda*(x1-x3)-y1
		return (x3%MOD,y3%MOD)
def mul(P, n, MOD):
	Q=P
	R=O
	while (n > 0):
		print(Q,R)
		if n % 2 == 1: R=add(R,Q,MOD)
		Q=add(Q,Q,MOD)
		n//=2
	return R
def prime_mod_sqrt(a, p):

    """
    Square root modulo prime number
    Solve the equation
        x^2 = a mod p
    and return list of x solution
    http://en.wikipedia.org/wiki/Tonelli-Shanks_algorithm
    """
    a %= p

    # Simple case
    if a == 0:
        return [0]
    if p == 2:
        return [a]

    # Check solution existence on odd prime
    if legendre_symbol(a, p) != 1:
        return []

    # Simple case
    if p % 4 == 3:
        x = pow(a, (p + 1)//4, p)
        return [x, p-x]

    # Factor p-1 on the form q * 2^s (with Q odd)
    q, s = p - 1, 0
    while q % 2 == 0:
        s += 1
        q //= 2

    # Select a z which is a quadratic non resudue modulo p
    z = 1
    while legendre_symbol(z, p) != -1:
        z += 1
    c = pow(z, q, p)

    # Search for a solution
    x = pow(a, (q + 1)//2, p)
    t = pow(a, q, p)
    m = s
    while t != 1:
        # Find the lowest i such that t^(2^i) = 1
        i, e = 0, 2
        for i in range(1, m):
            if pow(t, e, p) == 1:
                break
            e *= 2

        # Update next value to iterate
        b = pow(c, 2**(m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    return [x, p-x]


def legendre_symbol(a, p):
    ls = pow(a, (p - 1)//2, p)
    return -1 if ls==p-1 else ls
    

    
q_x=4726
n_b=6534
q_y=prime_mod_sqrt(cal(q_x),p)
print(cal(q_x)%p)
print("gg")
print(q_y)
Q=(q_x,q_y[0])
print(Q)
shared_secret = mul(Q,n_b,p)
iv ="cd9da9f1c60925922377ea952afc212c"
ciphertext="febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"

print(decrypt_flag(shared_secret[0], iv, ciphertext))
