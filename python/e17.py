nums = {
    0 : "",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
}
    
def val(x):
    
    st = str(x)
    ln = len(st)
    if ln == 4:
        return (len(nums[int(st[0])]) + len("thousand") + val(int(st[1:])))
    elif ln == 3:
        t = (len(nums[int(st[0])]) + len("hundred"))
        y = val(int(st[1:]))
        if y != 0:
            return t + len("and") + y
        else:
            return t
    elif ln == 2:
        if x >= 20:
            return (len(nums[int(st[0])*10])) + val(int(st[1:]))
        else:
            return len(nums[x])
    else:
        return len(nums[x])

sum = 0
n = 1000

for i in range(1, n+1):
    temp = val(i)
    print i, temp
    sum += temp
    
print sum