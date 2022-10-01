import sys
input=sys.stdin.readline

N=int(input())
array=list(map(int, input().split()))

M=1
def gcd(n,m):
    if m==0:
        return n
    elif m>0:
        return gcd(m, n%m)

#최소공배수
def lcm(n,m):
    return n*m//gcd(n,m)

answer=1
for i in range(N):
    answer=lcm(array[i], answer)

print(answer)

