'''
1 2 3 4 5 6 7 일때 
t=1일때는 바로 죽음
2부터 게임을 시작 2**3=8 => 3이 죽음
3 3**3=27 27을 외치는 애가 죽음
4 4**3=64를 외치는 애가 죽음
(t**3) mod len(queue) 그 다음에 죽일 애의 수
그냥 시뮬레이션 돌리면 됨 기말에는 삭제 방법이 다름
1억을 줄수도 있음 
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

def sol(n):
    circle, sequence = [i for i in range(1, n+1)], []
    j=0
    k=1
    while len(circle)>0:
        j=(j+(k**3)-1)%len(circle)
        sequence.append(circle.pop(j))
        k+=1
    return sequence[-1]

print(sol(n))
