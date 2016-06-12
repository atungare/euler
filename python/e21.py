import math

n = 10000

def div(x):
    if x == 0:
        return -1
    elif x == 1:
        return 1
    else:
        d = 0
        for i in range(1, int(x/2)+1):
            if x % i == 0:
                d += i
        return d

divs = []
sum = 0

for i in range(0, n):
    divs.append(div(i))


for i in range(0, n):
    d = divs[i]
    d2 = 0
    if d < n:
        d2 = divs[d]
    if i == d2 and d != d2:
        print i, d, d2
        sum += i

print sum