import sys
input = sys.stdin.readline
'''
def solve(n):
    print(n, end = " ")
    s = str(n)
    if len(s) > 1:
        prod = 1
        for i in range(len(s)):
            prod *= int(s[i]) 
        solve(prod)
'''
def fac(n):
    if len(str(n))==1: # 길이가 1이면 return 
        return n
    print(n, end=" ")
    s=str(n)
    if len(s)>1:
        multi=1
        for i in range(len(s)): # 각 자리수를 곱해준다
            multi*=int(s[i])
        return fac(multi)

while 1:
    n = int(input())
    if n==0:
        break
    print(fac(n))
