"""
ECC format
y^2=x^3 + ax + b (mod p)
"""
a=497
b=1768
p=9739
O=(0,0)
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

P=(493, 5564)
Q=(1539, 4742)
R=(4403, 5202)
print(add(add(add(P,P,p),Q,p),R,p))

P=(2339, 2213)
print(mul(P,7863,p))

Q_a=(815, 3190)
n_b=1829
print(mul(Q_a,n_b,p)[0])

