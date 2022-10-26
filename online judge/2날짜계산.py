# 윤년을 고려한 날짜 계산 
# X년 1월 1일에 시작해서 Y년 12월 31일에 종료
import sys
sys.stdin.readline

x=int(input())
y=int(input())

answer=0
while 1:
    if x>y:
        break
    if x%4==0 and x%100!=0: #윤년일때
        answer+=366
        x+=1
    elif x%400==0:# 윤년일때
        answer+=366
        x+=1
    else: # 윤년이 아닐때
        answer+=365
        x+=1

print(answer)

