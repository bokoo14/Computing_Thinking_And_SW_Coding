import sys
input = sys.stdin.readline

def fac(n):
    if len(str(n))==1:
        return n
    print(n, end=" ")
    s=str(n)
    if len(s)>1:
        multi=1
        for i in range(len(s)):
            multi*=int(s[i])
        return fac(multi)

while 1:
    n = int(input())
    if n==0:
        break
    print(fac(n))
