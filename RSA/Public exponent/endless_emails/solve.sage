n=[]
e=3
c=[]
with open("output.txt",'r') as f:
	for lines in f:
		if lines[0] == 'n': n.append(int(lines.strip()[3:]))
		elif lines[0] == 'c': c.append(int(lines.strip()[3:]))
print(len(n))
print(len(c))

N=prod(n)
n_min=min(n)
b1=vector([(n_min**i)*c[i] for i in range(e+1)]+[1/(e+1)])
b2=vector([N]+[0]*4)
b3=vector([0]*1+[(n_min**1)*N]+[0]*3)
b4=vector([0]*2+[(n_min**2)*N]+[0]*2)
b5=vector([0]*3+[(n_min**3)*N]+[0]*1)

print(b1.parent())
a=matrix([b1,b2,b3,b4,b5])
print(a.parent())
tmp=a.LLL()
print(tmp[0])

def linearPaddingHastads(cArray,nArray,aArray,bArray,e=3,eps=1/8):
    """
    Performs Hastads attack on raw RSA with no padding.
    This is for RSA encryptions of the form: cArray[i] = pow(aArray[i]*msg + bArray[i],e,nArray[i])
    Where they are all encryptions of the same message.
    cArray = Ciphertext Array
    nArray = Modulus Array
    aArray = Array of 'slopes' for the linear padding
    bArray = Array of 'y-intercepts' for the linear padding
    e = public exponent
    """
    if(len(cArray) == len(nArray) == len(aArray) == len(bArray) == e):
        for i in range(e):
            cArray[i] = Integer(cArray[i])
            nArray[i] = Integer(nArray[i])
            aArray[i] = Integer(aArray[i])
            bArray[i] = Integer(bArray[i])
        TArray = [-1]*e
        for i in range(e):
            arrayToCRT = [0]*e
            arrayToCRT[i] = 1
            TArray[i] = crt(arrayToCRT,nArray)
        P.<x> = PolynomialRing(Zmod(prod(nArray)))
        gArray = [-1]*e
        for i in range(e):
            gArray[i] = TArray[i]*(pow(aArray[i]*x + bArray[i],e) - cArray[i])
        g = sum(gArray)
        g = g.monic()
        # Use Sage's inbuilt coppersmith method
        roots = g.small_roots(epsilon=eps)
        if(len(roots)== 0):
            print("No Solutions found")
            return -1
        return roots[0]

    else:
        print("CiphertextArray, ModulusArray, and the linear padding arrays need to be of the same length," +
         "and the same size as the public exponent")



print(linearPaddingHastads(c[:3],n[:3],[1,1,1],[0,0,0]))
