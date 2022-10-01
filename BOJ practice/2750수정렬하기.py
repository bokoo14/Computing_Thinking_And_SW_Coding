import sys
input = sys.stdin.readline

N = int(input())
array=[int(input()) for _ in range(N)]

array.sort()

for i in range(N):
    print(array[i])

