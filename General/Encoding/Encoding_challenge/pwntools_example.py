from pwn import * # pip install pwntools
import json
from Crypto.Util.number import long_to_bytes
from base64 import b64decode
import string

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

cnt=0
while cnt < 100:

	received = json_recv()

	print("Received type: ")
	print(received["type"])
	print("Received encoded value: ")
	print(received["encoded"])

	def b64(s):
		return b64decode(s)
	def hex2b(s):
		return bytes.fromhex(s)
	def bigint(s):
		return long_to_bytes(s)
	def rot13(s):
		alphabet=string.ascii_lowercase
		shift=13
		ms=[]
		for i in s:
			if i.isalpha():
				tmp=ord(i)-ord('a')
				if tmp > 12:
					ms.append(alphabet[tmp-shift])
				else: ms.append(alphabet[tmp+shift])
			else :ms.append(i)
		return "".join(ms)
	def utf(s):
		return bytes(s)

	if received["type"] == "base64":
		res=b64(received["encoded"]).decode()
	if received["type"] == "hex":
		res=hex2b(received["encoded"]).decode()
	if received["type"] == "bigint":
		res=bigint(int(received["encoded"],16)).decode()
	if received["type"] == "utf-8":
		res=utf(received["encoded"]).decode()
	if received["type"] == "rot13":
		res=rot13(received["encoded"])
	to_send = {
	    "decoded": "{}".format(res)
	}
	json_send(to_send)

	cnt+=1
json_recv()
