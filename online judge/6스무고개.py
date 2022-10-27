import sys
input = sys.stdin.readline
'''
n, m = map(int,input().split())
x=int(input())

def sol(first, last):
    if first>last:
        return 
    mid = (first+last)//2
    if mid == x:
        print(x, "END")
        return 0

    if mid<x:
        print(mid, "UP")
        return sol(mid+1, last)
    else:
        print(mid, "DOWN")
        return sol(first, mid-1)
    

answer= sol(n,m)
'''
n, m= map(int, input().split())
x = int(input())

def sol(first, last):
    if first>last:
        return 
    mid = (first+last)//2

    if mid == x:
        print(x, "END")
        return x, "END"

    if x < mid: # 찾는 값이 더 작으면
        print(mid, "DOWN")
        return sol(first, mid-1)
    else:
        print(mid, "UP")
        return sol(mid+1, last)

answer=sol(n, m) 