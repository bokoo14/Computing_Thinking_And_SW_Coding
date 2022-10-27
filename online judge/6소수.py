import sys
import math
input = sys.stdin.readline
'''
t= int(input())
array=[0]*t
for i in range(t):
    array[i] = int(input())

# 에라토스테네스체를 이용한 소수찾기
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
'''
t = int(input())
num = [0]*t
for i in range(t):
    num[i]=int(input())

# 에라토스테네스체를 이용한 소수찾기
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
    if sieve[i]==1: # 소수라면 answer에 저장 
        answer.append(i)

def sol(find, first, last):
    if first>last:
        print("-1")
        return
    mid = (first+last)//2 # 인덱스값

    if find == answer[mid]:
        print(mid) # 인덱스값을 출력 - 몇번째 소수인지
        return mid
    
    if find < answer[mid]:
        return sol(find, first, mid-1)
    else:
        return sol(find, mid+1, last)

for i in range(t):
    sol(num[i],0, len(answer))
