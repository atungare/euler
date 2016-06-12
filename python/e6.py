import math

sum = 0
sum_squared = 0

for i in range(1, 101):
    sum += i
    sum_squared += (i**2)

print sum_squared - sum*sum