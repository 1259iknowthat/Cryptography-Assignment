import os
from Crypto.Util.Padding import pad
from datetime import datetime, timedelta
flag = 'crypto{testing_test}'.encode()
expires_at = (datetime.today() + timedelta(days=1))
cookie = f"admin=False;expiry={expires_at}".encode()
padded = pad(cookie, 16)
print(padded[:16])
