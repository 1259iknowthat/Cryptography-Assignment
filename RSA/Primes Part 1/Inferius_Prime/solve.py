#This code is contributed by tranminhprvt01
from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes, inverse
import math as mt


n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373



p=752708788837165590355094155871
q=n//p

phi=(p-1)*(q-1)
d=inverse(e,phi)
pt=long_to_bytes(pow(ct,d,n))

print(pt)






