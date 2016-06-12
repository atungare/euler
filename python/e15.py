n = 20
lat = [[-1 for x in range(n+1)] for y in range(n+1)]

def lattice(n1, n2):
    if lat[n1][n2] != -1:
        return lat[n1][n2]
    else:
        if (n1 < 0) or (n2 < 0):
            return 0
        if (n2 == 0 and n1 == 1) or (n1 == 0 and n2 == 1):
            return 1   
        else:
            lat[n1][n2] = lattice(n1-1, n2) + lattice(n1, n2-1)
            return lat[n1][n2]


print lattice(n, n)