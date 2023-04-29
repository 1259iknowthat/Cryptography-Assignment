p = 65537
a = 2732467876546

#Apply little Fermat theorem we got any integer x^(p-1) = 1 (mod p)  (with p is a prime)
print(pow(a, p-1, p))
