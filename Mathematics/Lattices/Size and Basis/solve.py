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
	def __mul__(self, num):
		n=len(self)
		if type(num) in [int,float]:
			return vector([num*self.coordinate[i] for i in range(n)])
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
	def size(self):
		return math.sqrt(vector.inner(self, self))

v = vector([4, 6, 2, 5])
print(v.size())
