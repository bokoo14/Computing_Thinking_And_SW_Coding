import sys
input=sys.stdin.readline
# 콜라츠 추측
def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0: # 짝수이면 x(i+1)=x(i)/2
        return [n] + collatz(n // 2)
    else: # 홀수이면 x(i+1)=3*x(i)+1
        return [n] + collatz(3*n + 1)

# 처음으로 같은 숫자가 나왔을때, 각각 몇번째 수열에서 만나는지 구해줌
def solve(A, B):
    a = collatz(A)[::-1]
    b = collatz(B)[::-1]
    minlen = min(len(a), len(b)) 
    i=0
    while True:
        if i == minlen or a[i] != b[i]:
            break
        i += 1
    return len(a) - i, len(b) - i, a[i - 1]

while True:
    A, B = map(int, input().split()) 
    if A == 0 and B == 0:
        break
    a1, a2, a3 = solve(A, B)
    print(f"{A} needs {a1} steps, {B} needs {a2} steps, they meet at {a3}")
