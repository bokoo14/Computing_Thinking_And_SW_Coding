import sys
input=sys.stdin.readline

n=int(input()) 

# 모든 양의 정수 N의 모든 약수의 합을 구하기
def solution(n):
    # answer = 0
    sum = 0 
    # 1~n까지 약수인지 아닌지 check
    for i in range(1, n+1):
        if n % i == 0: # 주어진 값 n이 i로 나누어지면 약수이다
            sum += i # 약수이면 그 값을 sum에 더함
            # answer = sum
    
    return sum

print(solution(n))
