fibs = [1, 1]
n = 0
a = str(fibs[n+1])

while len(a) < 1000:
    new = fibs[n] + fibs[n+1]
    fibs.append(new)
    a = str(new)
    n += 1

print len(fibs)