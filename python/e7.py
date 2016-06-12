import math

primes = []
n = 2

while len(primes) <= 10000:
    isPrime = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            isPrime = False
    if isPrime:
        primes.append(n)
    n += 1

print len(primes)
print primes
print primes.pop()