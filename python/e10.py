import math

primes = []
n = 2
sum = 0

while n <= 2000000:
    isPrime = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            isPrime = False
            break
    if isPrime:
        sum += n
    n += 1
    
print sum