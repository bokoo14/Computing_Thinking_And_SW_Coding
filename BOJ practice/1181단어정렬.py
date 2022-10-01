import sys
input = sys.stdin.readline

N = int(input())
array = [input().strip() for _ in range(N)]

array=set(array)
array=list(array)
array.sort(key = lambda x: (len(x), x))

for i in range(len(array)):
    print(array[i])
