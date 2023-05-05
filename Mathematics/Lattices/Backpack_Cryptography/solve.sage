#This code is contributed by tranminhprvt01
fi=open("output.txt",'r')
public=fi.readline().strip()
public=public[13:-1].split(', ')
ls=list(public)
ls=[int(i) for i in ls]
print(len(ls))
enc=int(fi.readline().strip()[16:])
print(enc)

def gen_matrix(arr):
	n=len(arr)
	#make n+1 * n+1 matrix
	cnt=0
	v=[]
	while cnt < n:
		v.append(vector([0]*cnt+[2]+[0]*(n-cnt-1)+[arr[cnt]]))
		#print(v[cnt],v[cnt].parent())
		cnt+=1
	v.append(vector([1]*n+[enc]))
	A=matrix([i for i in v])
	return A	
	
A = gen_matrix(ls)

B=A.LLL()

v=B[273-16]

print(v)

x=A.solve_left(v)

#print(x)


v_=[]
for i in v[:-1]:
	v_.append(str(0 if i^^1 == 0 else 1 ))

print(v_)
v_="".join(v_)[::-1]
v_=int(v_,2)
print(v_)

from Crypto.Util.number import long_to_bytes
	
print(long_to_bytes(v_))





