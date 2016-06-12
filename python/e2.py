evenSum = 0
fib = 1
next = 2
while fib < 4000000:
    if fib % 2 == 0:
        evenSum += fib
    temp = next
    next += fib
    fib = temp
print evenSum