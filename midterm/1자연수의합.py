import sys

def Sum(n):
    return n*(n+1)//2


# 1-1
a = Sum(2**10-1)
b = Sum(2**20)
answer = b-a
print("1-1")
print(answer)

# 1-2
c = Sum(2**30-1)
d = Sum(2**40)
answer = d-c
print("1-2")
print(answer)


# 1-3
'''
윤년 계산을 해서 날짜 부터 구한다
날짜를 이용해 자연수의 합을 구한다
'''
x = 1970
y = 2022
answer=0
money = 1
while 1:
    if x>y:
        break
    if x%4==0 and x%100!=0: #윤년일때
        for i in range (366):
            answer += money
            money+=1
        x+=1
    elif x%400==0:# 윤년일때
        for i in range (366):
            answer += money
            money+=1
        x+=1
    else: # 윤년이 아닐때
        for i in range (365):
            answer += money
            money+=1
        x+=1

print("1-3")
print(answer)
