import sys
input = sys.stdin.readline

n = int(input())
A=[list(map(int, input().split())) for _ in range(n)]
m, p = map(int, input().split())

# 행렬의 곱
def mul(n, m, A, B):
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
            C[i][j]%=m
    return C

def divAndConquer(n,m,p,A):
    if p == 1:
        return A
    elif p%2==0: # 짝수이면
        B = divAndConquer(n, m, p//2, A)
        return mul(n, m, B, B)
    else: # 홀수이면
        B = divAndConquer(n, m, p//2, A)
        return mul(n, m, A, mul(n, m, B, B))


answer= divAndConquer(n,m,p,A)
for i in range(n):
    print(*answer[i])

