a = 3
p = 13

"""
a^(p-1) = 1 mod p
a^(p-1) * a^-1 = a^-1 mod p
a^(p-2) = a^-1 mod p
"""

d=pow(a,p-2,p)
print(d)
