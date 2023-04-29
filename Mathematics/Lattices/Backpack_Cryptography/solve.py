import random
from collections import namedtuple
import gmpy2
from Crypto.Util.number import isPrime, bytes_to_long, inverse, long_to_bytes

fi=open("output.txt",'r')
public=fi.readline().strip()
public=public[13:-1].split(', ')
ls=list(public)
ls=[int(i) for i in ls]
print(len(ls))
enc=int(fi.readline().strip()[16:])
print(enc)



FLAG = b'abc'
PrivateKey = namedtuple("PrivateKey", ['b', 'r', 'q'])

def gen_private_key(size):
    s = 10000
    b = []
    for _ in range(size):
        ai = random.randint(s + 1, 2 * s)
        assert ai > sum(b)
        b.append(ai)
        s += ai
    while True:
        q = random.randint(2 * s, 32 * s)
        if isPrime(q):
            break
    r = random.randint(s, q)
    assert q > sum(b)
    assert gmpy2.gcd(q,r) == 1
    return PrivateKey(b, r, q)


def gen_public_key(private_key: PrivateKey):
    a = []
    for x in private_key.b:
        a.append((private_key.r * x) % private_key.q)
    return a


def encrypt(msg, public_key):
    assert len(msg) * 8 <= len(public_key)
    ct = 0
    msg = bytes_to_long(msg)
    for bi in public_key:
        ct += (msg & 1) * bi
        msg >>= 1
    return ct

def decrypt(ct, private_key: PrivateKey):
    ct = inverse(private_key.r, private_key.q) * ct % private_key.q
    msg = 0
    for i in range(len(private_key.b) - 1, -1, -1):
         if ct >= private_key.b[i]:
             msg |= 1 << i
             ct -= private_key.b[i]
    return long_to_bytes(msg)

private_key = gen_private_key(len(FLAG) * 8)
public_key = gen_public_key(private_key)
encrypted = encrypt(FLAG, public_key)
print(encrypted)
decrypted = decrypt(encrypted, private_key)
print(decrypted)
print(private_key)

"""
class vector:
	def __init__(self,array):
		self.coordinate=array
	def __str__(self):
		#print(self.coordinate,type(self.coordinate))
		return f"{self.coordinate}"
	def __add__(a,b):
		assert len(a) == len(b)
		n=len(a)
		return vector([a.coordinate[i] + b.coordinate[i] for i in range(n)])
	def __sub__(a,b):
		assert len(a) == len(b)
		n=len(a)
		return vector([a.coordinate[i] - b.coordinate[i] for i in range(n)])
	def __mul__(self, other):
		n=len(self)
		if type(other) in [int,float]:
			return vector([other*self.coordinate[i] for i in range(n)])
	def __len__(self):
		return len(self.coordinate)
	def __getitem__(self,n):
		return self.coordinate[n]
	def inner(a,b):
		#tich vo huong 2 vector
		assert len(a) == len(b)
		n=len(a)
		res=0
		for i in range(n):
			res+=a.coordinate[i]*b.coordinate[i]
		return res


def gram_schmidt(u):
	v=[u[0]]
	n=len(u)
	for i in range(1,n):
		res=vector([0]*VECTOR_SIZE)
		#print(res)
		for j in range(i):
			res+=v[j]*(vector.inner(u[i],v[j])/vector.inner(v[j],v[j]))
			#print("hahahha",i,j,res)
		v.append(u[i]-res)
	return v


def LLL(basis):
	#return reduce basis {v1,v2,...,vn} from {u1,u2,...,un} of lattice
	n=len(basis)
	k=2
	u=[basis[i] for i in range(k)]
	while k <= n:
		v=gram_schmidt(u)
		for j in range(k-1,0,-1):
			print("vector u",*u)
			print("vector v",*v)
			print(j,k,n)
			print("testing",)
			x=math.floor(vector.inner(u[k-1],v[j-1])/vector.inner(v[j-1],v[j-1]))
			print(f"uy k,j {x}")
			u[k-1]=u[k-1]-u[j-1]*x
			print("vector u again",*u)
			print("vector v again",*v)
		y=vector.inner(u[k-1],v[k-2])/vector.inner(v[k-2],v[k-2])
		if vector.inner(v[k-1],v[k-1]) >= (0.75-y*y)*vector.inner(v[k-2],v[k-2]): 
			print("ngu vc")
			k+=1
			u.append(basis[k-1])
		else:
			print("ok gg")
			u[k-1], u[k-2] = u[k-2], u[k-1]
			print("vector u after swap",*u)
			k=max(k-1,2)
	return u
	
VECTOR_SIZE=6
u1=vector([2, 0, 0, 0, 0, 89])
u2=vector([0, 2, 0, 0, 0, 243])
u3=vector([0 ,0, 2, 0, 0, 212])
u4=vector([0, 0, 0, 2, 0, 150])
u5=vector([0, 0, 0, 0, 2, 245])
u6=vector([1, 1, 1, 1, 1, 546])
basis=[u1,u2,u3,u4,u5,u6]

print(LLL(basis))
"""


	




