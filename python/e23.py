from math import sqrt
upper = 28123

def div(x):
    d = 0
    y = sqrt(x)
    for i in range(2, int(y)+1):
        if x % i == 0:
            d += i + (x / i)
    if y == int(y):
        d -= y
    return d

abuns = set()
sum = 0

for i in range(1, upper):
    notSum = True
    for a in abuns:
        if i-a in abuns:
            notSum = False
    if div(i) > i:
        abuns.add(i)
    if notSum:
        sum += i

print sum