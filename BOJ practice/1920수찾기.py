import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


def sol(array, num, first, last):
    if first>last:
        return 0
    mid = (first+last)//2
    if array[mid]==num:
        return 1
    elif num < array[mid]:
        return sol(array, num, first, mid-1)
    else:
        return sol(array, num, mid+1, last)


A.sort()
for i in range(m):
    print(sol(A, B[i], 0, len(A)-1))



'''
n = int(input())
A=set(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

for i in range(0, m):
    if B[i] in A:
        print("1")
    else:
        print("0")
'''