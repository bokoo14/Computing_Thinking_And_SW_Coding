import sys
inpit = sys.stdin.readline

m,n = map(int, input().split())

def is_prime(k):
    if k<2:
        return False
    else:
        for c in range(2, int(k**(0.5))+1):
            if k%c==0:
                return False
    return True

for i in range(m, n+1):
    answer=is_prime(i)
    if answer:
        print(i)
