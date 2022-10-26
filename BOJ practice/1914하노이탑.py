import sys
input = sys.stdin.readline

n=int(input()) # 원판의 개수

'''
def hanoi(N, start, middle, end):
    if N==0:
        return 
    elif N==1:
        print(start, end, sep=" ")
    else: 
        hanoi(N-1, start, end, middle)
        hanoi(1, start, middle, end)
        hanoi(N-1, middle, start, end)
'''

def hanoi(n, start, middle, end):
    if n==1:
        print(start, end)
    else:
        hanoi(n-1, start, end, middle)
        print(start, end)
        hanoi(n-1, middle, start, end)

print(2**n-1) # 옮긴 횟수
if n<=20: # n이 20 이하인 입력에 대해서만 수행 과정을 출력
    hanoi(n, 1, 2, 3)

