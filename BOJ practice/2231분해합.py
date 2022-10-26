import sys
input = sys.stdin.readline

# 분해합 구하기
'''
N = int(input())

answer = 0
answer += N

N = str(N)
N = list(map(int, N))
answer += sum(N)

print(answer)
'''
# 생성자 구하기
N = int(input()) #분해합이 주어짐 (216)

def solve(n):
    for m in range(1, n + 1): # 1~216까지 모두 check
        if n == m + sum(map(int, str(m))): # 216=198+1+9+8
            return m # 198을 return
        
    return 0 # 생성자가 없는 경우 0을 return

print(solve(N))