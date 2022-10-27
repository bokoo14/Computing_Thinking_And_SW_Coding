import sys
input = sys.stdin.readline

n = int(input())

def sol(n):
    low, high = 0, n
    while low <= high:
        mid = (low+high)//2
        if mid**2 >=n: # 제곱을 한 값이 더 크다면 
            high = mid-1
        else: # 제곱을 한 값이 더 작다면 
            low = mid +1
    return low 

print(sol(n))
