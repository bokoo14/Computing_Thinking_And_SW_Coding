import sys
input = sys.stdin.readline

N = int(input())
array=[int(input()) for _ in range(N)]

array.sort() # 오름차순 정렬
# s = sorted(array)
for i in range(N):
    print(array[i])
