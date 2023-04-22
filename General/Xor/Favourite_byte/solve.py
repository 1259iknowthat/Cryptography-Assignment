c = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
c = bytes.fromhex(c)

key = c[0] ^ ord("c") #First byte will be xor with c in "crypto{...}"

m = bytes([i ^ key for i in c])

print(m)
