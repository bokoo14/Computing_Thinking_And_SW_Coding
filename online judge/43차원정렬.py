import sys
input = sys.stdin.readline
n=int(input())

array = [list(map(int, input().split())) for _ in range(n)]

array.sort(key = lambda x : (x[0], -x[1], x[2]))

for i in range(n):
    print(*array[i])