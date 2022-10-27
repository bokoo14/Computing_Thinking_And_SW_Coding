import sys
input= sys.stdin.readline
'''
t = int(input())

array = [0]*(t)
for i in range(t):
    array[i]=int(input())


def fib(n):
    f=[0, 1] +[0]*(n-1)
    for i in range(2, n+1):
        f[i]=f[i-1]+f[i-2]
    return f

fiboArray=fib(50000)

def sol(first, last, find):
    if first>last:
        return -1

    mid = (first+last)//2

    if fiboArray[mid]==find:
        return mid
    if fiboArray[mid]<find:
        return sol(mid+1, last, find)
    else:
        return sol(first, mid-1, find)

for i in range(t):
    print(sol(0,50000, array[i]))
'''
t = int(input())
num = [0]*t 
for i in range(t):
    num[i] = int(input())

def fib(n):
    f=[0, 1] +[0]*(n-1)
    for i in range(2, n+1):
        f[i]=f[i-1]+f[i-2]
    return f

fiboArray=fib(50000) # 피보나치 수 50000개 만들기

def sol(find, first, last):
    if first>last:
        print(-1)
        return -1
    mid = (first+last)//2 # 인덱스 값

    if find == fiboArray[mid]: #값끼리 비교
        print(mid) #몇번째 피보나치 수열인지 알고 싶으면 인덱스 값을 출력
        return 
    if find < fiboArray[mid]: # 찾는 값이 더 작으면
        return sol(find, first, mid-1)
    else:
        return sol(find, mid+1, last)

for i in range(t):
    sol(num[i], 0, 50000)