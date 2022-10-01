import sys
sys.stdin.readline

x=int(input())
y=int(input())

answer=0
while 1:
    if x>y:
        break;
    if x%4==0 and x%100!=0: #윤년일때
        answer+=366
        x+=1
    elif x%400==0:# 윤년일때
        answer+=366
        x+=1
    else:
        answer+=365
        x+=1

print(answer)

