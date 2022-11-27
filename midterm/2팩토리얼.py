import sys

# 2-1
n, r = 1234567, 890

def permute(n, r):
    # 종료조건
    if r == 0: 
        return 1
    # 재귀조건
    else:
        return n * permute(n-1, r-1)

# print(permute(n, r))
print(str(permute(n, r))[:5])


# 2-2
def fac(n):
    if n<2:
        return 1
    else:
        return n*fac(n-1)

n, r = 1234567, 1234321
answer = permute(n, n-r) * fac(r)
print(answer)
