import sys
input = sys.stdin.readline

# 분할정복을 이용한 거듭제곱 𝑝𝑜𝑤𝑒𝑟(𝑎, 𝑏)

def power(a, b):
    if b == 1:
        return a
    elif b%2==0:
        c = power(a, b//2)
        return c*c
    else:
        c = power(a, b//2)
        return a*c*c

print(power(2, 1024))
print(2**1024)