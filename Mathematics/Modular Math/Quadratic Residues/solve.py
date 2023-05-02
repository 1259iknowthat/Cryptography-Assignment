p = 29
ints = [14, 6, 11]

for _ in ints:
    print(_,end=':\n')
    for i in range(p):
        t=(_+p*i)**0.5
        if(int(t)==t):
            print(t,end=' ')
    print()
