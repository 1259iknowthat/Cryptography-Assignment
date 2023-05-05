#This code is contributed by tranminhprvt01
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from Crypto.Util.number import getPrime, GCD, bytes_to_long, long_to_bytes, inverse
from random import randint



p, q = 10699940648196411028170713430726559470427113689721202803392638457920771439452897032229838317321639599506283870585924807089941510579727013041135771337631951, 11956676387836512151480744979869173960415735990945471431153245263360714040288733895951317727355037104240049869019766679351362643879028085294045007143623763
n = p * q

"""
# Alice side
v = (p * randint(1, n)) % n
k_A = randint(1, n)
while GCD(k_A, n) != 1:
    k_A = randint(1, n)
vka = (v * k_A) % n

# Bob side
k_B = randint(1, n)
while GCD(k_B, n) != 1:
    k_B = randint(1, n)
vkakb = (vka * k_B) % n

# Alice side
vkb = (vkakb * inverse(k_A, n)) % n

# Bob side
v_s = (vkb * inverse(k_B, n)) % n

# Alice side
key = sha256(long_to_bytes(v)).digest()
cipher = AES.new(key, AES.MODE_ECB)
m = pad(FLAG, 16)
c = cipher.encrypt(m).hex()


print(c)

print(v)
print(v_s)

"""

vka = 124641741967121300068241280971408306625050636261192655845274494695382484894973990899018981438824398885984003880665335336872849819983045790478166909381968949910717906136475842568208640203811766079825364974168541198988879036997489130022151352858776555178444457677074095521488219905950926757695656018450299948207 
vkakb = 114778245184091677576134046724609868204771151111446457870524843414356897479473739627212552495413311985409829523700919603502616667323311977056345059189257932050632105761365449853358722065048852091755612586569454771946427631498462394616623706064561443106503673008210435922340001958432623802886222040403262923652 
vkb = 6568897840127713147382345832798645667110237168011335640630440006583923102503659273104899584827637961921428677335180620421654712000512310008036693022785945317428066257236409339677041133038317088022368203160674699948914222030034711433252914821805540365972835274052062305301998463475108156010447054013166491083 
c = 'fef29e5ff72f28160027959474fc462e2a9e0b2d84b1508f7bd0e270bc98fac942e1402aa12db6e6a36fb380e7b53323'

print("n",n)


"""
n = p*q
v = (p*r) % n

vka = (v*ka) + k1*n  -  gcd(ka,n) = 1 => exist ka^-1 

vkakb = (vka*kb) % n = v*ka*kb + k2*n   - gcd(kb,n) = 1 => exit kb^-1

vkb = vkakb*ka^-1 = v*kb + k3*n

v_s = v



vka*vkb = v*v*ka*kb = v*vkakb  => vka*vkb*vkakb^-1 = v
xet tren mod q do gcd(vkakb, q) = 1

"""


"""
print(GCD(vkakb, q))

v = (vka*vkb*inverse(vkakb, q)) % n
print(v)
"""



"""
gcd(vka,vkakb) = v = 3*p
=> v is a multiple of p
divide everything by p
=> vkakb^-1 exist on mod n

after that we got (v / p) on mod n => multiply by p so we got v
"""

vka//=p
vkakb//=p
vkb//=p

print(GCD(vkakb,n))
v=((vka*vkb*inverse(vkakb,n)) % n * p) % n

print(v)

key = sha256(long_to_bytes(v)).digest()
cipher = AES.new(key, AES.MODE_ECB)
m = cipher.decrypt(bytes.fromhex(c))
print(m)




