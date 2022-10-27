'''
import sys
input = sys.stdin.readline

def sol(first, last, array):
    if first>last:
        return -1
    mid = (first+last)//2

    if array[mid]<array[mid+1] and array[mid]>array[mid-1]: #증가하는 부분
        return sol(mid+1, last, array) # 증가하는 구간이라면 오른쪽을 탐색
    elif array[mid]<array[mid-1] and array[mid]>array[mid+1]: # 감소하는 부분
        return sol(first, mid-1, array) # 감소하는 구간이라면 왼쪽을 탐색
    
    return mid

n = int(input())
array = [0]*n
for i in range(n):
    array[i] = int(input())

# print(array)
array2 = sorted(array)
array3 = sorted(array, reverse = True)
if n<3: # 원소의 수는 3이상
    print("-1")
elif array == array2: # 단조증가만 할 수 없음
    print("-1")
elif array == array3: # 단조 감소만 할 수 없음
    print("-1")
else:
    print(sol(0, len(array)-1, array))
'''

import sys
input = sys.stdin.readline

def sol(first, last, array):
    if first>last:
        return -1
    mid = (first+last)//2

    if array[mid]<array[mid+1] and array[mid]>array[mid-1]: #증가하는 부분
        return sol(mid+1, last, array) # 증가하는 구간이라면 오른쪽을 탐색
    elif array[mid]<array[mid-1] and array[mid]>array[mid+1]: # 감소하는 부분
        return sol(first, mid-1, array) # 감소하는 구간이라면 왼쪽을 탐색
    
    return mid

n = int(input())
array = [0]*n
for i in range(n):
    array[i] = int(input())

# print(array)
array2 = sorted(array)
array3 = sorted(array, reverse = True)
if n<3: # 원소의 수는 3이상
    print("-1")
else:
    print(sol(1, len(array)-2, array))


