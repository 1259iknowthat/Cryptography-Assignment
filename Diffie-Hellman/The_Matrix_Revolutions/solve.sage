P = 2
N = 150

def load_matrix(fname):
    data = open(fname, 'r').read().strip()
    rows = [list(map(int, row)) for row in data.splitlines()]
    return Matrix(GF(P), rows)
    

B_pub=load_matrix('bob.pub')
print(B_pub.parent())

G=load_matrix('generator.txt')

print(G)

#eigenval=list(G.eigenvalues())
#print(B_pub.eigenvalues())

print(G.multiplicative_order())
#find x such that G^x = I

print(G.parent())


