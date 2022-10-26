import sys
input = sys.stdin.readline

n = int(input())
array = [0]*n
for i in range(n):
    array[i] = int(input())

# print(array)

def sol(first, last, array):
    if first>last:
        return -1
    mid = (first+last)//2

    if array[mid]<array[mid+1] and array[mid]>array[mid-1]: #증가하는 부분
        return sol(mid+1, last, array)
    elif array[mid]<array[mid-1] and array[mid]>array[mid+1]: # 감소하는 부분
        return sol(first, mid-1, array)
    
    return mid

    
array2 = sorted(array)
array3 = sorted(array, reverse = True)
if n<3:
    print("-1")
elif array == array2:
    print("-1")
elif array == array3:
    print("-1")
else:
    print(sol(0, len(array)-1, array))
