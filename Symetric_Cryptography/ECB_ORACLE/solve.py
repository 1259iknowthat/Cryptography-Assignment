"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt(plaintext):
    plaintext = bytes.fromhex(plaintext)

    padded = pad(plaintext + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return {"error": str(e)}

    return {"ciphertext": encrypted.hex()}

KEY=b"vN0nb7ZshjAWiCzv"
FLAG="hellohellohelloh"
pt=b"abcdefghijklmnop"
print(len(pt),len(FLAG),len(pt)+len(FLAG))
pt=pt.hex()
a=encrypt(pt)
print(a)
b=pad(bytes.fromhex(pt) + FLAG.encode(), 16)
print(b,len(b))
for i in b:
	print(i)
"""
"""
#16 bytes dau tien cua ciphertext la  16 bytes cua known pt + flag
#vi the ta se chon known pt = 15 ki tu nao do sau do bf ki tu flag con lai
#sau do thay the lui de tim cac ki tu con lai cua flag
#
ct="eadf6148e03b6de994fb2c45ce68b5aca6734bcc83eace3a107321af7775026b7d715d5c670622e24c462ae108288f25"

#1 byte digit = 2 hex digit
print(ct[:32])
tmp=bytes.fromhex(ct)
print(tmp,len(tmp))
tmp=tmp[:16]
print(tmp,len(tmp))
#khoi tao known pt
knownpt=''.join(list("0" for i in range(15)))
print(knownpt,len(knownpt))

ct1="b56209aadbd75493cd818e01f8e98c51bea177bc81b326eef475195dee42ba6c2eb3958aa4a3fa0d49789f5152a4eed2"
print(ct1[:32])
print(ct1[32:64])
"""


import requests

flag=""

knownpt=b''.join(b"0" for i in range(31))
print(knownpt.hex())


while (len(knownpt) > 0):
	hex_string=knownpt.hex()
	URL=f"http://aes.cryptohack.org/ecb_oracle/encrypt/{hex_string}"
	r=requests.get(url = URL)
	data=r.json()
	enc=data["ciphertext"]
	print(f"enc {enc}")
	for i in range(33,126):
		if len(flag) != 0 : pt=knownpt+flag.encode()
		else : pt=knownpt
		pt+=chr(i).encode()
		hex_string=pt.hex()
		URL=f"http://aes.cryptohack.org/ecb_oracle/encrypt/{hex_string}"
		print(hex_string,len(hex_string))
		r=requests.get(url = URL)
		data=r.json()
		enc1=data["ciphertext"]
		print(pt,i,len(pt))
		if (enc[:64] == enc1[:64]):
			print(i)
			print(enc)
			print(enc1)
			print(enc[:64])
			print(enc1[:64])
			flag+=chr(i)
			break
	#print(flag,flag.hex())	
	knownpt=knownpt[:-1]
print(bytes.fromhex(flag))
#lay duoc 1 ki tu dau cua flag





