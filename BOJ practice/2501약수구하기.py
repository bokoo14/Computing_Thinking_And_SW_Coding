import sys
input = sys.stdin.readline
'''
def solve(n, k):
    cnt = 0
    for d in range(1, n + 1):
        # n을 d로 나누었을 때 나머지가 0이면 d는 n의 약수
        if n % d == 0: 
            cnt += 1 
            if cnt == k: # k번째 약수 구하기
                return d
    return 0

N, K = map(int, input().split())
print(solve(N, K))
'''
# 모든 약수를 탐색하는 더 효율적인 방법
def divisor(n): 
    div = set()
    # 1~루트n까지만 check
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0: # 약수이면 
            div.add(d)
            div.add(n // d)
    return sorted(list(div))

N, K = map(int, input().split())
D = divisor(N)
print(D[K - 1] if K <= len(D) else 0)
# 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을출력
