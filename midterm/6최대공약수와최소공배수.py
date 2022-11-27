import sys

import random
SEED, MIN, MAX, N = 2022, 100, 1000, 100
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)
# print(S)

# 최대공약수
def gcd(n,m):
    if m==0:
        return n
    elif m>0:
        return gcd(m, n%m)


#최소공배수
def lcm(n,m):
    return n*m//gcd(n, m)