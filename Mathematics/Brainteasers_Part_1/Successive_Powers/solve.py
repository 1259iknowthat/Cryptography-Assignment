"""
i=1
while (i < 3):
	n=588**(2*i)-665
	k=1
	print("cc")
	print(n)
	while len(str(n//k)) > 3:
		k+=1
	print(k)
	print(n/k)
	while n//k >= 851:
		if n%k != 0 : continue
		print(i,n,k,n/k)
		k+=1
	i+=1
"""

for p in range(1,114*2091000):
	if 588**2 % p == 665:
		print(p)
