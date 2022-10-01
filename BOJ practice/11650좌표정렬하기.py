import sys
input = sys.stdin.readline

N =int(input())

array = [tuple(map(int, input().split())) for _ in range(N)]
array.sort(key=lambda x: (x[0], x[1]))

array = list(array)
for i in range(N):
    print(*array[i])
'''
import sys

N = int(sys.stdin.readline())

points = []
for i in range(0, N):
    points.append(list(sys.stdin.readline().split()))

points.sort(key=lambda x:int(x[1]))
points.sort(key=lambda x:int(x[0]))

for i in range(0, N):
    print(points[i][0], points[i][1])
'''