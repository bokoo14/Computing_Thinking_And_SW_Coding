import sys
input = sys.stdin.readline

# 처음으로 계란이 깨지는 가장 낮은 층의 높이 T구하기
def eggdrop(n, T):
    global cnt
    cnt += 1
    return n >= T # 계란이 깨지면 True, 안 깨지면 False

def solve(N, T):
    low, high = 1, N 
    while low <= high:
        mid = (low + high) // 2
        if eggdrop(mid, T):
            high = mid - 1
        else:
            low = mid + 1
    return low



