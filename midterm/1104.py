import sys

'''
ncm의 철사가 주어졌다
이 철사로 삼각형을 만들자
단 각 변의 길이는 정수다
n = 9일때 경우의 수는?
1) a+b+c=n
2) a<=b<=c
3) a+b>c

삼각형의 성립 조건
a, b, c 가 변의 길이이고 c가 제일 긴 길이라고 한다면
c < a + b 이면 삼각형이 성립됨.
'''

# 1
# 코드가 느리다!
n=10
answer=0
for a in range(1, n):
    for b in range(a, n):
        for c in range(b, n):
            if a+b+c ==n and a+b>c:
                print(a, b, c)
                answer+=1
print(answer)


# 2
cnt2=0
for a in range(1, n):
    for b in range(a, n):
        c=n-a-b
        if b<=c and a+b>c:
            cnt2+=1

print(cnt2)

# 3
n=10000
cnt3=0
for x in range((n+1)//3, (n+1)//2):
    for y in range((n-x+1)//2, x+1):
        cnt3+=1

print(cnt3)

# 4
n=1000000
cnt4=0
for x in range((n+1)//3, (n+1)//2):
    cnt4+= x-(n-x+1)//2+1

print(cnt4)



'''
1~n까지의 자연수가 있다.
중복은 없다
그런데, 한 개를 잊어버렸다
몇 번째 수인지 찾는 방법은?
: (n)(n+1)/2 - 모두 다 더한 값을 빼줘라

1~n까지의 자연수가 있다.
중복은 없다
그런데, 연속된 두 개를 잊어버렸다
몇 번째 수인지 찾는 방법은?
...


카데인 알고리즘
: 부분 배열의 합 찾기


'''
