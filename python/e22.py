import names22

names = sorted(names22.names)
sum = 0

def val(let):
    return ord(let) - 64
    
def wordScore(word):
    count = 0
    for letter in word:
        count += val(letter)
    return count

for i in range(0, len(names)):
    sum += (i+1)*wordScore(names[i])

print sum