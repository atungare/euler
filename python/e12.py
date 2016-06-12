import math

facts = []
n = 1
tri = 0

while len(facts) < 500:
    tri += n
    facts = []
    for i in range(1, int(math.sqrt(tri))+1):
        if tri % i == 0:
            facts.append(i)
            if tri/i not in facts:
                facts.append(tri/i)
    n += 1
print tri, len(facts)