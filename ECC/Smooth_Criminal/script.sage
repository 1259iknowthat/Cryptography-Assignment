

# Define the curve
p = 310717010502520989590157367261876774703
a = 2
b = 3



# Construct curve on sage
F = GF(p)
E = EllipticCurve(F, [a,b])

g_x = 179210853392303317793440285562762725654
g_y = 105268671499942631758568591033409611165
G = E(g_x, g_y)
print(G.order())

# Get public value A = G*n
fi=open("output.txt",'r')
data=fi.readline().rstrip()
data=data[6:-1]
data=data.split(", ")
A_x, A_y = int(data[0][2:]), int(data[1][2:])
A=E(A_x, A_y)
print(A)

# Compute n
n = discrete_log(A,G,G.order(),operation='+')
print(f"Found n = {n}")
