import sys

n=int(sys.stdin.readline())
array = list(map(str, input()))

#print(array)

idx = -1
def get_next(s):
    global idx
    idx += 1
    return s[idx]

T = [[0]*n for _ in range(n)]
def quadtree(i, j, n, s, T):
    head = get_next(s)
    if head == "W" or head == "B":
        for r in range(i, i + n):
            for c in range(j, j + n):
                T[r][c] = 0 if head == "W" else 1
    else:
        m = n // 2
        quadtree(i, j, m, s, T) 
        quadtree(i, j+m, m, s, T) 
        quadtree(i+m, j, m, s, T) 
        quadtree(i+m, j+m, m, s, T)

quadtree(0, 0, n, array, T)

for i in range(n):
    for j in range(n):
        print(T[i][j], end = "")
    print("")
    