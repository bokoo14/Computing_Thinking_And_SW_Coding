import sys
input=sys.stdin.readline

# 최대 공약수 구하기
def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

# 모든 약수 구하기
def divisor(n): 
    div = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0: # 나누어 떨어지면 약수
            div.add(d)
            div.add(n // d)
    return sorted(list(div))

def solve(n, A):
    G = gcd(A[0], A[1]) # 두 값의 최대 공약수 구하기
    if N == 3: # input이 3개라면 세 값의 최대 공약수 구하기
        G = gcd(G, A[2])
        
    #최대 공약수 값인 G의 모든 약수값을 구하기
    for d in divisor(G):
        print(d)

N = int(input())
A = list(map(int, input().split()))
solve(N, A)