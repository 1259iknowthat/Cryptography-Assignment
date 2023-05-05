#This code is contributed by tranminhprvt01
import math
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
def Gauss(v1, v2):
	while True:
		if vector.inner(v2,v2) < vector.inner(v1,v1) : v1, v2 = v2, v1
		m = math.floor(vector.inner(v1,v2) / vector.inner(v1,v1))
		print(m,v1,v2)
		if m == 0 : return v1, v2
		v2 = v2 - v1*m
		
v1=vector([846835985, 9834798552])
v2=vector([87502093, 123094980])

u, v = Gauss(v1,v2)
print(vector.inner(u, v))

	
