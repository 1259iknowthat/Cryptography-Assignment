def check(k, p):
	for n in range(2, p):
		if pow(k, n, p) == k:
			return False
	return True

p = 28151

for k in range(p):
	if check(k, p):
		print(k)
		break

