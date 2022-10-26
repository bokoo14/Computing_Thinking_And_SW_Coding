import sys

N=int(sys.stdin.readline())
A=[list(map(int, input().split())) for _ in range(N)]

def check(i, j, n, A):
    chk = A[i][j]
    for r in range(i, i + n):
        for c in range(j, j + n):
            if A[r][c] != chk:
                return 2
    return chk

def quadtree(i, j, n, A):
    if n == 1:
        return str(A[i][j])
    else:
        chk = check(i, j, n, A)
        if chk < 2: #같으면
            if chk==1:
                return "B"
            elif chk==0:
                return "W"
        #return str(chk) 
        else: # 다르면
            m = n//2
            s1 = quadtree(i, j, m, A)
            s2 = quadtree(i,j+m , m, A)
            s3 = quadtree(i+m, j , m, A)
            s4 = quadtree( i+m, j+m , m, A)
            return "Q" + s1 + s2 + s3 + s4


def solve(n, A):
    return quadtree(0, 0, n, A)


answer = str(solve(N, A))
answer = list(answer)

for i in range(len(answer)):
    if answer[i]=="1":
        answer[i]="B"
    elif answer[i]=="0":
        answer[i] = "W"

print(N)
for i in range(len(answer)):
    print(answer[i], end = "")



   