import sys
input= sys.stdin.readline
'''
n= int(input())

array=[0]*n
for i in range(n):
    array[i]=int(input())

def sol(first, last):
    if first>last:
        print(-1)
        return -1
    mid = (first+last)//2

    if array[mid]==mid:
        print(mid)

    elif array[mid]<mid:
        return sol(mid+1, last)
    else:
        return sol(first, mid-1)

answer=sol(0, n-1)
'''
x = int(input())
nums = [0]*x
for i in range(x):
    nums[i] = int(input())

def sol(first, last):
    if first>last:
        print("-1")
        return -1

    mid = (first+last)//2
    if mid == nums[mid]: # 제자리수라면
        print(mid)
        return 1

    if nums[mid] < mid: # 찾는 값이 더 작다면 
        return sol(first, mid-1)
    else: # 찾는 값이 더 크다면
        return sol(mid+1, last)

sol(0, x-1)

    