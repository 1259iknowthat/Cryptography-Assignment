def xor(a : bytes, b : bytes):
	#a is key
	tmp = a
	while len(a) < len(b):
		a+=tmp
	if len(a) > len(b) : a=a[:len(b)]
	assert len(a) == len(b)
	return bytes([i ^ j for i, j in zip(a, b)])

m = b"crypto{"
c = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

key = xor(m,c[:len(m)])
print(key)
key+=b'y'

m = xor(key, c)

print(m)


