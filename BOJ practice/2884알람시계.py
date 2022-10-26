'''
알람 시각보다 45분 일찍 설정하기
'''
import sys
input=sys.stdin.readline

H, M = map(int, input().split())

def alarm(h, m):
    if (m-45)>=0: #45보다 큰 값이면 그냥 minute을 뺴주면 된다
        m=m-45
        h=h
    else: # 45보다 작은 값이면 
        m=(m-45)%60 #45를 빼주고 60으로 나눠준 나머지를 계산
        h=(h-1)%24 #45분보다 작으니까 1hour를 빼준다

    return h, m

hour, minute = alarm(H, M)
print(hour, minute)
