import sys
input = sys.stdin.readline

ara = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
rom = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

# 로마 숫자를 아라비아 숫자로 
def to_arabic(r):
    n = 0
    for i in range(len(r)):
        if (i<len(r)-1) and ara[r[i]]<ara[r[i+1]]:
            n-=ara[r[i]]
        else:
            n+=ara[r[i]]

    return n


# 아라비아 숫자를 로마 숫자로
def to_roman(a):
    nums = list(rom.keys())
    strs = list(rom.values())
    r = ""
    for i in range(len(rom)):
        while a >= nums[i]:
            r += strs[i]
            a -= nums[i]
    return r

# 소인수 분해
def factorization(arabic):
    d = 2
    while d<=arabic:
        if arabic%d==0:
            print(to_roman(d))
            arabic = arabic //d
        else:
            d = d+1


arabic = to_arabic(input().strip())
factorization(arabic)

