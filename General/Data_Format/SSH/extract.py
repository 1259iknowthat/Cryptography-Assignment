#convert ssh public key to .pem

#convert .der to .pem

import os

cmd="ssh-keygen -f bruce_rsa.pub -e -m pem > bruce_rsa.pem"
os.system(cmd)


from Crypto.PublicKey import RSA

f=open("bruce_rsa.pem",'r').read()

key=RSA.importKey(f)

print("n = ",key.n)
print("e = ",key.e)
print("d = ",key.d)
print("p = ",key.p)
print("q = ",key.q)

