import sys
input = sys.stdin.readline
n=int(input())

array = list(map(str, input().split()))

# array.sort(key = lambda x: len(x))

# 자리수 정렬, 내림차순 정렬
array.sort(key = lambda x: (len(x), -int(x)))
print(*array)
