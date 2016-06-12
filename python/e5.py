import math

n = 20
facts = []
prod = 1

for i in range(2, n+1):
    for j in facts:
        if i % j == 0:
            i /= j
    facts.append(i)
            
for num in facts:
     prod *= num

print sorted(facts)
print prod
