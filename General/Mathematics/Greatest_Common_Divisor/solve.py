def gcd(a, b):
	#print(a, b)
	if a == 0: return b
	if a < b : a, b = b, a
	return gcd(a%b,b)
	
	
a = 66528
b = 52920
print(gcd(a, b))
