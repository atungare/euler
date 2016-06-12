n = 100

fact = 1
sum = 0

for i in range(1, n+1):
    fact *= i

while fact != 0:
    sum += fact % 10
    fact /= 10

print sum