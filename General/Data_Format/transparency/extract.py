from Crypto.PublicKey import RSA

f=open("transparency.pem",'r').read()

key=RSA.importKey(f)

print("n = ",key.n)
print("e = ",key.e)

"""
print("d = ",key.d)
print("p = ",key.p)
print("q = ",key.q)
"""

