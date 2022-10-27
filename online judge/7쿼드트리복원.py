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


n=int(sys.stdin.readline())
array = list(map(str, input()))
T = [[0]*n for _ in range(n)]
quadtree(0, 0, n, array, T)

for i in range(n):
    for j in range(n):
        print(T[i][j], end = "")
    print("")
    