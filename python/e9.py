c = 1000

while c > 0:
    for b in range (0, c):
        for a in range (0, b):
            if (a*a+b*b == c*c) and (a+b+c == 1000):
                print a
                print b
                print c
                print a*b*c
    c -= 1