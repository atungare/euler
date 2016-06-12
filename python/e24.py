import itertools

digits = "0123456789"

perms = list(itertools.permutations(digits, 10))

print "".join(perms[999999])