import sys
input = sys.stdin.readline

l, m, n = map(int, input().split())

A=[list(map(int, input().split())) for _ in range(l)]
B=[list(map(int, input().split())) for _ in range(m)]

C = [[0]*n for _ in range(l)]
for i in range(l):
    for j in range(n):
        for k in range(m):
            C[i][j]+=A[i][k]*B[k][j]

for i in range(l):
    print(*C[i])


