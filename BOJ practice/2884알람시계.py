import sys
input=sys.stdin.readline

H, M = map(int, input().split())

def alarm(h, m):
    if (m-45)>=0:
        m=m-45
        h=h
    else:
        m=(m-45)%60
        h=(h-1)%24

    return h, m

hour, minute = alarm(H, M)
print(hour, minute)