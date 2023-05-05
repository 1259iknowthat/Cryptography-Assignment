#This code is contributed by tranminhprvt01
from math import sqrt
def factors(n):    
    j = 2
    while n > 1:
        for i in range(j, int(sqrt(n+0.05)) + 1):
            if n % i == 0:
                n //= i ; j = i
                yield i
                break
        else:
            if n > 1:
                yield n; break


                
x = 851 - 642

x = 588*209 - 665 #this x will equal k*p so now we factorize this to find p which is 3-digits 

ls = [i for i in factors(x)]
print(ls)