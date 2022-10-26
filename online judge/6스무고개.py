import sys
input = sys.stdin.readline

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