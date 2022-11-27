import sys
sys.setrecursionlimit(10**6) #재귀 제한 풀기
input = sys.stdin.readline

N=4

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-3)+2*fibo(n-2)-fibo(n-1)
       


print(fibo(N))
