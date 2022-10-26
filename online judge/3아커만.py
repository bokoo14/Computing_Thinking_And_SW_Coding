import sys
sys.setrecursionlimit(10**6) #재귀 제한 풀기
input = sys.stdin.readline

N, M=map(int, input().split())

# 아커만 함수
def ack(n, m):
    if n==0:
        return m+1
    elif n>0 and m==0:
        return ack(n-1,1)
    elif n>0 and m>0:
        return ack(n-1, ack(n,m-1))

print(ack(N,M))