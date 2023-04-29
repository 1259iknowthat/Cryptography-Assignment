from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long, inverse
import random
from math import gcd
from sympy import prod
primes=[106979, 108533, 69557, 97117, 103231]

c=20304610279578186738172766224224793119885071262464464448863461184092225736054747976985179673905441502689126216282897704508745403799054734121583968853999791604281615154100736259131453424385364324630229671185343778172807262640709301838274824603101692485662726226902121105591137437331463201881264245562214012160875177167442010952439360623396658974413900469093836794752270399520074596329058725874834082188697377597949405779039139194196065364426213208345461407030771089787529200057105746584493554722790592530472869581310117300343461207750821737840042745530876391793484035024644475535353227851321505537398888106855012746117
n=21711308225346315542706844618441565741046498277716979943478360598053144971379956916575370343448988601905854572029635846626259487297950305231661109855854947494209135205589258643517961521594924368498672064293208230802441077390193682958095111922082677813175804775628884377724377647428385841831277059274172982280545237765559969228707506857561215268491024097063920337721783673060530181637161577401589126558556182546896783307370517275046522704047385786111489447064794210010802761708615907245523492585896286374996088089317826162798278528296206977900274431829829206103227171839270887476436899494428371323874689055690729986771
e=0x10001
d=2734411677251148030723138005716109733838866545375527602018255159319631026653190783670493107936401603981429171880504360560494771017246468702902647370954220312452541342858747590576273775107870450853533717116684326976263006435733382045807971890762018747729574021057430331778033982359184838159747331236538501849965329264774927607570410347019418407451937875684373454982306923178403161216817237890962651214718831954215200637651103907209347900857824722653217179548148145687181377220544864521808230122730967452981435355334932104265488075777638608041325256776275200067541533022527964743478554948792578057708522350812154888097

#calculate p, q => phi  with given e, d, N
#https://www.di-mgt.com.au/rsa_factorize_n.html
print(e)
def find(N, e, d):
	while True:
		g=random.randrange(N)
		#print(g<N)
		k=e*d-1
		t=k
		
		while (t % 2 == 0):
			t//=2
			x=pow(g,t,N)
			y=gcd(x-1,N)
			if (x > 1 and y > 1): 
				p=y
				q=N//y
				return p, q
p, q=find(n, e, d)
phi=(p-1)*(q-1)

"""
c0=m^p0 mod N
c1=c0^p1 mod N
..
c4=c3^p4 mod N


c1=m^(p0*p1) mod N

=> c4 = m^(p0*...*p4) mod N
"""
print(p,q)
print(phi)
new_e=prod(primes)
print(new_e)
new_d=pow(new_e,-1,phi)
print(new_d)
m=pow(c,new_d,n)
print(long_to_bytes(m))





