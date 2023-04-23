from Crypto.Util.number import inverse

p = 991
g = 209

d = inverse(g, p)

print(d)

