import math

num = 600851475143

facts = []
lim = int(math.sqrt(num)) + 1

for i in range (2, lim):
    while num % i == 0:
        num = num / i
        facts.append(i)

print facts.pop()