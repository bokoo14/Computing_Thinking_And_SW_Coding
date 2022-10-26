import sys
import math
input = sys.stdin.readline

#약수의 개수 구하기
def divcnt(n):
    cnt=0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0: #약수일때
            cnt+=2
    if int(math.sqrt(n))**2 == n: # 제곱수일때 두번 더해지니까
        cnt-=1 # 한번 빼줌

    return cnt


n, m = map(int, input().split())
# 약수의 개수가 가장 많은 수와 그 수의 약수의 개수 출력하기
maxcnt, maxval = 0, 1
for i in range(n, m+1):
    cnt=divcnt(i) #약수의 개수
    if cnt>=maxcnt: #약수 개수 최대값
        maxcnt, maxval=cnt, i

print(maxval) #약수 제일 많은 수
print(maxcnt) #약수의 개수


