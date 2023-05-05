#This code is contributed by tranminhprvt01
from Crypto.Util.number import inverse, long_to_bytes


with open("output.txt",'r') as f:
	for lines in f:
		if lines[0] == "n" : n=int(lines.rstrip()[3:])
		elif lines[0] == "e": e=int(lines.rstrip()[3:])
		elif lines[0] == "c": c=int(lines.rstrip()[3:])


print(n)
print(e)
print(c)


p=34857423162121791604235470898471761566115159084585269586007822559458774716277164882510358869476293939176287610274899509786736824461740603618598549945273029479825290459062370424657446151623905653632181678065975472968242822859926902463043730644958467921837687772906975274812905594211460094944271575698004920372905721798856429806040099698831471709774099003441111568843449452407542799327467944685630258748028875103444760152587493543799185646692684032460858150960790495575921455423185709811342689185127936111993248778962219413451258545863084403721135633428491046474540472029592613134125767864006495572504245538373207974181
q=n//p

phi=(p-1)*(q-1)
d=inverse(e,phi)

flag=pow(c,d,n)

print(long_to_bytes(flag))




