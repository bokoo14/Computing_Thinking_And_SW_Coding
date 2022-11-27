import sys
input=sys.stdin.readline

def sebo(n):
    if n<4:
        return n
    else:
         a, b, c = 1, 2, 3
         for _ in range(4,n+1):
            a, b, c = b, c, a+b+c
    return c

n=int(input())
print(sebo(n))