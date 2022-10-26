import sys
input = sys.stdin.readline

N = int(input())

def solve(n):
    m, cnt = n, 1
    while True:
        s = sum(map(int, list(str(m)))) # 각 자리수의 합
        m = (m % 10) * 10 + (s % 10) # (가장 오른쪽 자리 수) + (앞에서 구한 합의 가장 오른쪽 자리 수) 
        if m == n: # 원래의 수로 돌아온다면 
            break
        cnt += 1
    return cnt # 사이클 길이

print(solve(N)) # 사이클 길이