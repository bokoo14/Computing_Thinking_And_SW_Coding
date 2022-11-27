import sys
input = sys.stdin.readline

# 다음 값을 가져옴
idx = -1
def get_next(s):
    global idx
    idx += 1
    return s[idx]

def quadtree(i, j, n, s, T):
    head = get_next(s)
    if head == "W" or head == "B": # 값이 모두 0 또는 1이라면
        for r in range(i, i + n):
            for c in range(j, j + n):
                T[r][c] = 0 if head == "W" else 1
    else: # 값이 섞여있으면 4개로 쪼갠다
        m = n // 2
        quadtree(i, j, m, s, T) 
        quadtree(i, j+m, m, s, T) 
        quadtree(i+m, j, m, s, T) 
        quadtree(i+m, j+m, m, s, T)


n=16
array = "QWBQBQWQWWBWWWQBWWBQBWWBQBQWWQWBWWWQBWWBQBWWB"
T = [[0]*n for _ in range(n)]
quadtree(0, 0, n, array, T)

sum = 0
for i in range(n):
    for j in range(n):
        print(T[i][j], end = " ")
        sum+=T[i][j]
    print("")
    
print(sum)

'''
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

ccccc=0
for i in range(len(answer)):
    if answer[i]=="1":
        answer[i]="B"
        ccccc+=1
    elif answer[i]=="0":
        answer[i] = "W"

print(N)
for i in range(len(answer)):
    print(answer[i], end = "")



print(ccccc)

'''
   