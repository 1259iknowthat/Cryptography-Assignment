#This code is contributed by tranminhprvt01
import random

def long_to_bytes(s):
	return s.to_bytes(1, 'big')

def bytes_to_binary(s):
    bin_str = ''.join(format(b, '08b') for b in s)
    bits = [int(c) for c in bin_str]
    return bits

def generate_mat():
    while True:
        msg = bytes_to_binary(FLAG)
        msg += [random.randint(0, 1) for _ in range(N*N - len(msg))]
        #print(len(msg))
        print(msg)

        rows = [msg[i::N] for i in range(N)]
        print(rows)
        mat = Matrix(GF(2), rows)
        print(mat)
        return mat
        break

        if mat.determinant() != 0 and mat.multiplicative_order() > 10^12:
            return mat
            
def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row)) for row in data.splitlines()]
    return Matrix(GF(P), rows)

def print_mat(A):
	print('\n'.join(''.join(str(i) for i in rows) for rows in A))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def mod_inv(a,p):
	#a*u+b*v = 1 if (gcd(a,b)=1)
	#a*u = 1 mod b
	# 
	gcd, u, v= egcd(a,p)
	print(gcd, u ,v)
	return u%p
	
def bin_to_bytes(s):
    all_bytes = [s[i:i+8] for i in range(0, len(s), 8)]
    return b''.join(long_to_bytes(int(byte, 2)) for byte in all_bytes)

P = 2
N = 50
E = 31337

A=load_matrix("flag.enc")
print(A)

g=multiplicative_order(A)
D=mod_inv(E,g)
print(D)
mat=A^D


cols = mat.columns()[:(34*8//50)+1]

bin_flag = ''.join([str(bit) for col in cols for bit in col])

print(bin_to_bytes(bin_flag))




