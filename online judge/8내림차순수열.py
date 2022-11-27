import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))

def sol(array):
    stack = []
    while len(array):
        cur = array.pop(0)
        # 더 작거나 같은 값들은 모두 pop
        while len(stack) and stack[-1]<=cur:
            stack.pop()
        stack.append(cur)

    return stack

answer = sol(array)
print(*answer)
        
