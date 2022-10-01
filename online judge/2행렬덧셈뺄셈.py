import sys
input=sys.stdin.readline

N, M = map(int, input().split())

A=[list(map(int, input().split())) for _ in range(N)]
B=[list(map(int, input().split())) for _ in range(N)]
C=[list(map(int, input().split())) for _ in range(N)]

D=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        D[i][j]=A[i][j]+B[i][j]-C[i][j]

for i in range(N):
    print(*D[i])


