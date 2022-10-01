import sys
input = sys.stdin.readline
n=int(input())

array = list(map(str, input().split()))

# array.sort(key = lambda x: len(x))

array.sort(key = lambda x: (len(x), -int(x)))
print(*array)
