from Crypto.Cipher import AES
from pwn import *

ct = bytes.fromhex("d1c3bcfeaeec552dfb180c45159fee1801be9ef81a7e1ac5fc937571d1b40738328e05c70fdc01b6a956934202b9aae7")
pt = bytes.fromhex("3b5624f4894d906b06bceac8d1d536f2b2b1c58eda832e1e987a537060fc852d5e8ae8c82b1a45f4cbcc5450f0952645")

iv = ct[:16]
ct1 = ct[16:32]
# ct2 = ct[32:]
pt1 = pt[16:32]
pt2 = pt[32:]
# print(len(pt1), len(pt2))
# print(len(ct1))
# print(len(iv))
data1 = xor(iv, pt1)
data2 = xor(ct1, pt2)
print(data1+data2)
