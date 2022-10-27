import sys
input = sys.stdin.readline
'''
n, m = map(int,input().split())
num=int(input())
x=list(map(int, input().split()))

cnt = 0
def sol(first, last, i):
    global cnt
    cnt+=1
    if first>last:
        return 
    mid = (first+last)//2
    if mid == x[i]:
        return 0

    if mid<x[i]:
        return sol(mid+1, last, i)
    else:
        return sol(first, mid-1, i)


for i in range(num):
    answer=sol(n, m, i)

print(cnt)
'''
n, m = map(int, input().split())
k = int(input())
answer = list(map(int, input().split()))

cnt = 0
def sol(answer, first, last):
    global cnt
    if first>last:
        return 0

    mid = (first+last)//2

    if answer == mid:
        cnt+=1
        return answer
    if answer<mid:
        cnt+=1
        return sol(answer, first, mid-1)
    else:
        cnt+=1
        return sol(answer, mid+1, last)


for i in range(k):
    sol(answer[i], n, m)

print(cnt)