s = b"label"
num = 13

t = bytes([i ^ num for i in s])

print(b"crypto{"+t+b"}")
