def xor(a : bytes, b : bytes):
	assert len(a) == len(b)
	return bytes([i ^ j for i, j in zip(a, b)])
	
k1  = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k21 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
c   = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


k1  = bytes.fromhex(k1)
k23 = bytes.fromhex(k23)
c   = bytes.fromhex(c)



print(xor(xor(c, k23), k1))
