import sys
import math
input = sys.stdin.readline

n= int(input())

# N의 모든 약수의 합 구하기
# 모든 N에 대해 검사를 하면 시간초과에 걸릴 수 있음
def divcnt(n):
    answer=0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i==0: # 나누어지면 약수이다
            answer+=i # 약수를 더해줌
            answer+=n//i #또 다른 약수도 더해줌(몫)
    if int(math.sqrt(n))**2 ==n: #값이 제곱수이면
        answer-=int(math.sqrt(n)) # 두번 더해졌으니까 한번 뺴줌
    return answer


print(divcnt(n))
