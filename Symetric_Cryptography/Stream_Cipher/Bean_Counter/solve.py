import os
class StepUpCounter(object):
    def __init__(self, value=os.urandom(16), step_up=False):
        self.value = value.hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.newIV = hex(int(self.value, 16) + self.step)
        else:
            #print(hex(int(self.value, 16) - self.stup))
            self.newIV = hex(int(self.value, 16) - self.stup)
        self.value = self.newIV[2:len(self.newIV)]
        return bytes.fromhex(self.value.zfill(32))
    
    def __repr__(self):
        self.increment()
        return self.value
    
        



ctr = StepUpCounter()
"""
print(ctr.value)
print(int(ctr.value, 16),ctr.stup)
print(ctr.stup)
print(ctr.increment(),len(ctr.increment()))
"""
out=[]
with open("test.txt",'rb') as f:
	block=f.read(16)
	while block:
		print(block)
		keystream=ctr.increment()
		print(keystream)
		xored = [a^b for a, b in zip(block, keystream)]
		print(xored)
		out.append(bytes(xored).hex())
		block=f.read(16)



print(out)

for i in out:
	print(list(bytes.fromhex(i)))
	
	
magic_number="89504e470d0a1a0a0000000d49484452"
print(len(magic_number))
print(bytes.fromhex(magic_number),len(bytes.fromhex(magic_number)))

import requests
import json

base_url = "http://aes.cryptohack.org/bean_counter"
r=requests.get(f"{base_url}/encrypt")
data=r.json()
enc=data["encrypted"]


fo=open("flag.png",'wb')
png_format=bytes.fromhex(magic_number)
ct=enc[:32]
ct=bytes.fromhex(ct)
xored=[a^b for a, b in zip(ct, png_format)]
keystream=bytes(xored)
print(keystream,len(keystream))

out=[]
while enc:
	ct=enc[:32]
	print(ct)
	ct=bytes.fromhex(ct)
	xored=[a^b for a, b in zip(ct, keystream)]
	#out.append(bytes(xored).hex())
	enc=enc[32:]
	fo.write(bytes(xored))
print(out)
fo.close()


