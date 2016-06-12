import math

pals = []

def isPal(n):
    st = str(n)
    rev = st[::-1]
    return st == rev

for i in range(100, 1000):
    for j in range (100, 1000):
        n = i*j
        if isPal(n):
            pals.append(n)

print sorted(pals)