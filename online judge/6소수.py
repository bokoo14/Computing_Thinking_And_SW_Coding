import sys
import math
input = sys.stdin.readline

t= int(input())
array=[0]*t
for i in range(t):
    array[i] = int(input())

def solve(M, N):
    global sieve
    sieve = [1]*(N+1) #리스트에 값을 저장
    sieve[0]=sieve[1]= 0 #0과 1은 소수가 아니다
    for i in range(2, int(math.sqrt(N))+1):
        if sieve[i] >= 0: #sieve의 값이 
            for j in range(i*i, N+1, i): # i의 배수들
                sieve[j]=0 #배수들을 -0로 바꿔줌(소수가 아님)
    
solve(0, 1000000)
answer=[0]
for i in range(1000000):
    if sieve[i]==1:
        answer.append(i)



def divide(first, last, find):
    if first>last:
        return -1
    mid = (first+last)//2 

    if answer[mid] == find:
        return mid

    if find > answer[mid]:
        return divide(mid+1, last, find)
    else:
        return divide(first, mid-1, find)

for i in range(t):
    print(divide(0, len(answer), array[i]))

