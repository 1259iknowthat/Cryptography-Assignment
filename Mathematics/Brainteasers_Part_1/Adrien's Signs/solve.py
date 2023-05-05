#This code is contributed by tranminhprvt01
from Crypto.Util.number import long_to_bytes

a = 288260533169915
p = 1007621497415251

with open("output.txt", "r") as f:
    v = eval(f.read())

res = ""
for x in v:
    c = pow(x, (p-1)//2, p)
    if c == 1:
        res += "1"
    else:
        res += "0"

print(long_to_bytes(int(res, 2)))
