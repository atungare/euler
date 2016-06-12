def feb(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return 29
        elif year % 100 == 0:
            return 28
        else:
            return 29
    else:
        return 28
        
def months(year):
    m = [31, feb(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m
    
def isSun(day):
    if day % 7 == 0:
        return True
    else:
        return False
    
jan_1900 = 1
mos_1900 = months(1900)

for i in range(0, len(mos_1900)):
    jan_1900 += mos_1900[i]

start = jan_1900
count = 0

for yr in range(1901, 2001):
    mos = months(yr)
    for m in range(0, len(mos)):
        if isSun(start):
            count += 1
        else:
            count += 0
        start += mos[m]

print count
    