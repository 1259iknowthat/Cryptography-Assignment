#convert .der to .pem

import os

cmd="openssl x509 -inform der -in 2048b_rsa_example_cert.der -out 2048b_rsa_example_cert.pem"
os.system(cmd)


from Crypto.PublicKey import RSA

f=open("2048b_rsa_example_cert.pem",'r').read()

key=RSA.importKey(f)

print("n = ",key.n)
print("e = ",key.e)
print("d = ",key.d)
print("p = ",key.p)
print("q = ",key.q)

