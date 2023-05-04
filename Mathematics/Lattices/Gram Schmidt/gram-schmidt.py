#This code is contributed by tranminhprvt01
class vector:
	def __init__(self,array):
		self.coordinate=array
	def __str__(self):
		#print(self.coordinate,type(self.coordinate))
		return f"{self.coordinate}"
	def __add__(a,b):
		assert len(a) == len(b)
		n=len(a)
		return vector([a.coordinate[i] + b.coordinate[i] for i in range(n)])
	def __sub__(a,b):
		assert len(a) == len(b)
		n=len(a)
		return vector([a.coordinate[i] - b.coordinate[i] for i in range(n)])
	def __mul__(self, other):
		n=len(self)
		if type(other) in [int,float]:
			return vector([other*self.coordinate[i] for i in range(n)])
	def __len__(self):
		return len(self.coordinate)
	def inner(a,b):
		#tich vo huong 2 vector
		assert len(a) == len(b)
		n=len(a)
		res=0
		for i in range(n):
			res+=a.coordinate[i]*b.coordinate[i]
		return res

def gram_schmidt(u,v):
	n=len(u)
	for i in range(1,n):
		res=vector([0]*VECTOR_SIZE)
		for j in range(i):
			res+=v[j]*(vector.inner(u[i],v[j])/vector.inner(v[j],v[j]))
			print(i,j,res)
		v.append(u[i]-res)
	return v
VECTOR_SIZE=4
u1=vector([4, 1, 3, -1])
u2=vector([2, 1, -3, 4])
u3=vector([1, 0, -2, 7])
u4=vector([6, 2, 9, -5])
u=[u1,u2,u3,u4]
v=[u1]

print(*u)
print(*v)

v=gram_schmidt(u,v)
print(*v)
print(round(v[3].coordinate[1],5))





