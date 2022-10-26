import sys
input = sys.stdin.readline

s, t = input().split()

s= sorted(list(s.upper())) # 모두 대문자로 변경
t = sorted(list(t.lower())) # 모두 소문자로 변경

c = s+t
#문자열을 기준으로 정렬, 같은 문자일때 소문자가 먼저 나와야 한다
c.sort(key = lambda x : (x.upper(), -ord(x)))

print(" ".join(map(str, c)))
