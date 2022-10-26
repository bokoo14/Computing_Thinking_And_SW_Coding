import sys
input = sys.stdin.readline

# 소수인지 판별 - 약수가 존재하지 않아야 소수이다
def is_prime(k):
    if k<2:
        return False
    else:
        for c in range(2, int(k**(0.5))+1):
            if k%c==0: # 약수가 존재한다면 소수가 아님
                return False
    return True

m,n = map(int, input().split())
# m~n의 소수를 모두 출력
for i in range(m, n+1):
    answer=is_prime(i)
    if answer: # 소수라면 출력
        print(i)
