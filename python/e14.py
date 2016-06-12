
def numSteps(n):
    count = 0
    while n != 1:
        count +=1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
    return count
    
greatestNum = 0
greatestSteps = 0

for i in range (1, 1000001):
    num = numSteps(i)
    if num > greatestSteps:
        greatestSteps = num
        greatestNum = i
        
print greatestNum