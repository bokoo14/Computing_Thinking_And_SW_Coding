# 윤년을 고려한 날짜 계산 
# X년 1월 1일에 시작해서 Y년 12월 31일에 종료
import sys
sys.stdin.readline

x=1970
y=2022

answer=0
cnt =0
money = 0
while 1:
    if x>y:
        break
    if x%4==0 and x%100!=0: #윤년일때
        answer+=366
        for i in range(366):
            cnt+=1
            money+=cnt
        x+=1
    elif x%400==0:# 윤년일때
        answer+=366
        for i in range(366):
            cnt+=1
            money+=cnt
        x+=1
    else: # 윤년이 아닐때
        for i in range(365):
            cnt+=1
            money+=cnt
        answer+=365
        x+=1



print(answer)
print(money)

