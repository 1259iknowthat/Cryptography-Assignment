"""
ECC format (Montgomery Curve)
By^2=x^3 + Ax^2 + x (mod p)
"""
A=486662
B=1
p=(2**255)-19
O=(0,0)
def cal(x):
	return x*x*x+A*x*x+x
	

def add(P,Q,MOD):
	#return P+Q
	assert P != Q
	x1=P[0]
	y1=P[1]
	x2=Q[0]
	y2=Q[1]
	a=(y2-y1)*pow(x2-x1,-1,MOD)
	x3=B*a*a-A-x1-x2
	y3=a*(x1-x3)-y1
	return (x3%MOD,y3%MOD)

def dbl(P,MOD):
	#return [2]P
	x1=P[0]
	y1=P[1]
	a=(3*x1*x1+2*A*x1+1)*pow(2*B*y1,-1,MOD)
	x3=B*a*a-A-2*x1
	y3=a*(x1-x3)-y1
	return (x3%MOD,y3%MOD)
	
def mul(P, k, MOD):
	#return [k]P
	print(k)
	A,B=P,dbl(P,MOD)
	l=len(str(bin(k))[2:])
	print(l)
	arr=list(str(bin(k))[2:])
	print(arr)
	assert arr[0] == '1'
	for i in range(1,l):
		if arr[i] == '0':
		
			B=add(A,B,MOD)
			A=dbl(A,MOD)
			
		else:
			A=add(A,B,MOD)
			B=dbl(B,MOD)
			
	return A
	
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

G_x=9
G_y=prime_mod_sqrt(cal(G_x),p)
G1=(G_x,G_y[0])
G2=(G_x,G_y[1])
print(G1)
print(G2)
Q1=mul(G1,0x1337c0decafe,p)
Q2=mul(G2,0x1337c0decafe,p)
print(Q1[0]%p)
print(Q2[0]==Q1[0])
print(Q1,Q2)
