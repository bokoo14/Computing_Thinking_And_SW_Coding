import sys
input = sys.stdin.readline
n=int(input())

array = [list(map(int, input().split())) for _ in range(n)]

# x좌표 증가하는 순, y좌표 감소하는 순, z좌표 증가하는 순
array.sort(key = lambda x : (x[0], -x[1], x[2]))

for i in range(n):
    print(*array[i])