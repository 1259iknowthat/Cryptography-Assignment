from Crypto.Cipher import AES
import hashlib

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


ct="c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"


with open("words") as f:
	words=[w.strip() for w in f.readlines()]

for i in words:
	pwd=hashlib.md5(i.encode()).hexdigest()
	tmp=decrypt(ct,pwd)
	ms=bytes.fromhex(tmp["plaintext"])
	if b"crypto" in ms :
		print(ms)

