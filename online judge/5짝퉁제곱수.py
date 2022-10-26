import sys
input = sys.stdin.readline
import math

# n의 각 자리수를 더하기
def plus(n):
    N=[int(i) for i in str(n)]
    return sum(N)

# 각 자리수의 합이 제곱수인지 판별
def mul(k):
    N = plus(k) # 각 자리수의 합
    if int(math.sqrt(N))**2 == N:
        return 1

    return 0

n, m = map(int, input().split())
answer=0
for i in range(n, m+1):
    if mul(i): # 짝퉁제곱수라면 count
        answer+=1

print(answer)
