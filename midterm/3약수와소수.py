import sys
import math
input = sys.stdin.readline

# 3-1
#약수의 개수 구하기
def divcnt(n):
    cnt=0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0: #약수일때
            cnt+=2
    if int(math.sqrt(n))**2 == n: # 제곱수일때 두번 더해지니까
        cnt-=1 # 한번 빼줌

    return cnt

# 소수인지 판별
def is_prime(k):
    if k<2:
        return False
    else:
        for c in range(2, int(k**(0.5))+1):
            if k%c==0: # 나누어지는 값이 있으면 약수가 있음 = 소수가 아님
                return False
    return True

n, m = 10000, 20000
cnt = 0
for i in range(n, m+1):
    cnt+=is_prime(divcnt(i))

print(cnt)

# 3-2
def divsum(n):
    s=0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0: #약수일때
            s+=i
            s+=n%i
    if int(math.sqrt(n))**2 == n: # 제곱수일때 두번 더해지니까
        s-=i # 한번 빼줌

    return s

