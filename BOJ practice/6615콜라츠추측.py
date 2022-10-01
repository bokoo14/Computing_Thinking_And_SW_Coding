import sys
input=sys.stdin.readline
def collatz(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n // 2)
    else:
        return [n] + collatz(3*n + 1)

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
