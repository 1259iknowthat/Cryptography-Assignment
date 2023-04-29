import requests

value = "qwertyuiopasdfghjklzxcvbnm{}_0123456789QWERTYUIOPASDFGHJKLZXCVBNM"

lst = []
pt = "00" * 31
padding = "00" * 31
tmp = ""
idx = 0
for i in range(32):
    padding = "00" * (31 - i)
    pt = pt[idx:]
    sign = requests.get(url = f"http://aes.cryptohack.org/ecb_oracle/encrypt/{padding}/")
    sign = sign.text.split(":")[1].replace('}','').strip()
    # print(padding, pt, idx)
    for c in value:
        p = str(hex(ord(c)))
        tmp = pt + p.replace('0x','')
        r = requests.get(url = f"http://aes.cryptohack.org/ecb_oracle/encrypt/{tmp}/")
        # print(c, end=" ")
        header = r.text.split(":")[1].replace('}','').strip()[1:53]
        if header in sign:
            print(padding, tmp, len(tmp))
            # print(header)
            lst.append(c)
            pt = tmp
            idx = 2
            print(c)
            break
print()
print(lst)
for i in lst:
    print(i,end="")