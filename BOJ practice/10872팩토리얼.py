#파이썬 최대 재귀 횟수는 1000번까지 가능
'''
현재 재귀 횟수의 상한을 가져옵니다.sys.getrecursionlimit()
재귀 횟수의 상한을 변경합니다.sys.setrecursionlimit()
스택의 최대 크기 변경:resource.setrlimit()
'''

import sys
sys.setrecursionlimit(15000) #재귀 제한 풀기
input = sys.stdin.readline

n=int(input())

def fac(N):
    if N==0: #종료조건
        return 1
    else:
        return N*fac(N-1)

answer= fac(n)
print(answer)