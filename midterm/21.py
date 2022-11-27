#파이썬 최대 재귀 횟수는 1000번까지 가능
'''
현재 재귀 횟수의 상한을 가져옵니다.sys.getrecursionlimit()
재귀 횟수의 상한을 변경합니다.sys.setrecursionlimit()
스택의 최대 크기 변경:resource.setrlimit()
'''

import sys
sys.setrecursionlimit(10**8) #재귀 제한 풀기
input = sys.stdin.readline

answer =1
for i in range(1, 1234567):
    answer *= i
    


answer2 =1
for i in range(1, 1233677):
    answer2 = answer2*i

answer= list(answer)
answer2= list(answer2)
print(answer[0:4])
print(answer2[0:4])
# print(int(answer//answer2))

