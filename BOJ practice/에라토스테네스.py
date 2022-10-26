import sys
input = sys.stdin.readline
import math
# N보다 작거나 같은 모든 소수를 효율적으로 찾는 알고리즘
'''
def solve(M, N):
    sieve = [1]*(N+1) #리스트에 값을 저장
    sieve[0]=sieve[1]= 0 #0과 1은 소수가 아니다

    for i in range(2, int(math.sqrt(N))+1):
        if sieve[i] >= 0: #sieve의 값이 소수라면
            for j in range(i*i, N+1, i): # i의 배수들
                sieve[j]=0 #배수들을 -0로 바꿔줌(소수가 아님)
    
    print(sieve)
    print(sum(sieve))

solve(1, 10)

'''
def find_primes(n):
    sieve = [0] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 0:
            for j in range(i * i, n + 1, i):
                sieve[j] = 1
    return [i for i in range(2, n + 1) if sieve[i] == 0]

print(find_primes(10))
print(find_primes(100))
