import sys
input = sys.stdin.readline

'''
# 1
N=int(sys.stdin.readline())
#video=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
video=[]
for i in range(0, N):
    video.append(list(map(int, sys.stdin.readline().strip())))


def quad(x, y, n):
    compare=video[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if compare!=video[i][j]:
                print("(", end="")
                quad(x, y, n//2)
                quad(x, y+n//2, n//2)
                quad(x+n//2, y, n//2)
                quad(x+n//2, y+n//2, n//2)
                print(")", end="")
                return
    print(compare, end="")

quad(0, 0, N)
'''
def quadtree(i, j, n, A): # x, y, box크기, 배열
    if n==1: # 박스를 쪼갤 수 없으면
        return str(A[i][j])
    else: # 박스를 쪼갤 수 있으면
        chk = check(i, j, n, A) # 압축할 수 있는지 체크
        if chk<2: # 값이 0이나 1이라면 - 압축할 수 있으면
            return str(chk)
        else:
            m = n//2
            s1 = quadtree(i, j, m, A)
            s2 = quadtree(i, j+m, m, A)
            s3 = quadtree(i+m, j, m, A)
            s4 = quadtree(i+m, j+m, m, A)
            return "("+s1+s2+s3+s4+")"

def check(i, j, n, A):
    chk = A[i][j]
    for r in range(i, i+n):
        for c in range(j, j+n):
            if A[r][c] != chk:
                return 2
    return chk


N = int(input()) 
A = [list(map(int, input().strip())) for _ in range(N)] 
print(quadtree(0, 0, N, A))
