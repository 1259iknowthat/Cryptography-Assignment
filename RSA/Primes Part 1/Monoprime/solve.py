#This code is contributed by tranminhprvt01
from Crypto.Util.number import *
f=open("output.txt",'r')
data=f.readlines()
cnt=0
for i in data:
	if cnt==0: n=int(i[4:-1])
	elif cnt == 1: e=int(i[4:-1])
	else: ct=int(i[4:-1])
	cnt+=1
print(n)
print(e)
print(ct)
phi=n-1
d=inverse(e,phi)
print(long_to_bytes(pow(ct,d,n)))
