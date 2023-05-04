#This code is contributed by tranminhprvt01
class vector
	def __init__(self,array)
		self.coordinate=array
	def __str__(self)
		#print(self.coordinate,type(self.coordinate))
		return f{self.coordinate}
	def __add__(a,b)
		assert len(a) == len(b)
		n=len(a)
		return vector([a.coordinate[i] + b.coordinate[i] for i in range(n)])
	def __sub__(a,b)
		assert len(a) == len(b)
		n=len(a)
		return vector([a.coordinate[i] - b.coordinate[i] for i in range(n)])
	def __mul__(self, num)
		n=len(self)
		if type(num) in [int,float]
			return vector([numself.coordinate[i] for i in range(n)])
	def __len__(self)
		return len(self.coordinate)
	def inner(a,b)
		#tich vo huong 2 vector
		assert len(a) == len(b)
		n=len(a)
		res=0
		for i in range(n)
			res+=a.coordinate[i]b.coordinate[i]
		return res

v = vector([2, 6, 3])
w = vector([1, 0, 0])
u = vector([7, 7, 2])

print(vector.inner((v*2 - w)*3, u2))
