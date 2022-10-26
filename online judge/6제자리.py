import sys
input= sys.stdin.readline

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
