#This code is contributed by tranminhprvt01
import json
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.number import *
from Crypto.Util.Padding import pad, unpad
def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row.split(' '))) for row in data.splitlines()]
    return Matrix(GF(P), rows)

P = 13322168333598193507807385110954579994440518298037390249219367653433362879385570348589112466639563190026187881314341273227495066439490025867330585397455471
N = 30  

G=load_matrix("generator.txt")

eigenval=list(G.eigenvalues())
eigenval=sorted(eigenval)
print(len(eigenval) == len(set(eigenval)))#show that eigenval has duplicate
for i in range(len(eigenval)-1):
	if eigenval[i] == eigenval[i+1]:
		dup=eigenval[i]
A, p=G.jordan_form(transformation=true)
print(A)
print(p)

data=json.load(open("output.txt",'r'))
v=vector(GF(P),data['v'])
w=vector(GF(P),data['w'])
v=~p*v
w=~p*w

print(dup)
data=json.load(open("flag.enc",'r'))
iv=data['iv']
enc=data['ciphertext']
iv=bytes.fromhex(iv)
enc=bytes.fromhex(enc)
KEY_LENGTH = 128


for i in range(N-1):
	w1=w[i]
	w2=w[i+1]
	v1=v[i]
	v2=v[i+1]
	secret=dup*(w1-v1*w2/v2)/w2 
	#secret%=P
	KEY = SHA256.new(data=str(secret).encode()).digest()[:KEY_LENGTH]
	cipher = AES.new(KEY, AES.MODE_CBC, iv)
	flag=cipher.decrypt(enc)
	print(flag,i)
"""
P=17
F=GF(P)
A=Matrix([[6,-2,-1],[3,1,-1],[2,-1,2]])
print(A)
eigenval=list(A.eigenvalues())
lamda=eigenval[0]
print(f"lamda {lamda}")

z=A.eigenvectors_right()
print(z,type(z))
z=vector(z[0][1])
print(z,type(z))
#print(A.is_diagonalizable())
J=A.jordan_form()
print(J)	
I=identity_matrix(3)
print(I)
B=(A-lamda*I)^2
print(B)
v=B.solve_right(z)
print(v)
"""
