#This code is contributed by tranminhprvt01
from math import prod
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt
"""
Hastad's Boardcast Attack
Summary:
+ given pair (Ni, ei). We have Ci=pow(M,ei,Ni)
Assume of all e = 3 and having >= 3 distinct equations
C1 = pow(M,3,N1) 
C2 = pow(M,3,N2)
C3 = pow(M,3,N3)

CRT => C = pow(M,3,N1*N2*N3)
if M^3 < N1N2N3 => M = C^(1/3)

C1=pow(M1,3,N1)
C2=pow(M2,3,N2)

"""


"""
length = 3
a = [2,3,5]
n = [5,11,17]

Ntot= n[0] * n[1] * n[2]

N = [ n[1]*n[2] , n[0]*n[2], n[0]*n[1] ]

y = [pow(N[i],n[i]-2,n[i]) for i in range(length)]

mysterious_a = 0
for i in range(length):
        mysterious_a += a[i]*N[i]*y[i]
mysterious_a %= Ntot
print(mysterious_a)
"""
from Crypto.Util.number import bytes_to_long, getPrime
from math import gcd
def CRT(a,n):
	Ntot=prod(n)
	N=[prod(n[:t]+n[t+1:]) for t in range(len(n))]
	y=[pow(N[i],n[i]-2,n[i]) for i in range(len(n))]
	
	mys_a=0
	for i in range(len(n)):
		mys_a+=a[i]*N[i]*y[i]
	mys_a%=Ntot
	return mys_a


n=[]
e=3
c=[]
with open("output.txt",'r') as f:
	for lines in f:
		if lines[0] == 'n': n.append(int(lines.strip()[3:]))
		elif lines[0] == 'c': c.append(int(lines.strip()[3:]))
print(len(n))
print(len(c))

def check(n):
	#this function for checking all modulus are co-prime with each other
	for i in range(len(n)):
		for j in range(i):
			if gcd(n[i],n[j]) != 1: 
				#print("vcccc")
				return False
	return True

res=[]

for i in range(len(n)-2):
	for j in range(i+1,len(n)-1):
		for k in range(j+1,len(n)):
			print(i,j,k)
			poss_c=[c[i],c[j],c[k]]
			poss_n=[n[i],n[j],n[k]]
			C=CRT(poss_c,poss_n)
			C_=crt(poss_n, poss_c)
			print(C,C_)
			#print(C_)
			tmp=iroot(C_[0],e)

			if tmp[1] == True:
				print(tmp)
				print(long_to_bytes(tmp[0]))
				if b'crypto{' in long_to_bytes(tmp[0]): res.append(long_to_bytes(tmp[0]))
			
print(res)







