from pwn import *

store = '1280d425f8ca35fb5bbdd7fdf68942771c961c3ff046d0bf0a0094842f83a3378211b1517959a3165a812fbe591a4d01'
pt = bytes.fromhex('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
ct = bytes.fromhex('1280d425f8ca35fb5bbdd7fdf68942771c961c3ff046d0bf0a0094842f83a3378211b1517959a3165a812fbe591a4d01')

ct1 = ct[:16]
# ct2 = ct[16:32]
# pt2 = pt[16:32]
# pt3 = pt[32:]
# dec2 = xor(pt2, ct1)
# dec3 = xor(pt3, ct2)

tmp_ct3 = ct1[:]
tmp_ct2 = b'\x00' * 16
tmp_ct = ct1 + tmp_ct2 + tmp_ct3
print(tmp_ct.hex())

invalid_pt = bytes.fromhex('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa017da76dff228caa00eee4aa1184626529b6cf1f7a156cbf22d197d6479af534')
key = xor(invalid_pt[:16], invalid_pt[32:])
print(key, key.hex())