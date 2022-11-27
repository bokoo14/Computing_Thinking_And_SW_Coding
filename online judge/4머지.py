import sys
input = sys.stdin.readline

s, t = input().split()

s= sorted(list(s.upper())) # 모두 대문자로 변경
t = sorted(list(t.lower())) # 모두 소문자로 변경

c = s+t
#문자열을 기준으로 정렬, 같은 문자일때 소문자가 먼저 나와야 한다
# A: 65 a: 97
# 대소문자 구분없이 정렬하고, 아스키코드 값을 이용해서 정렬
c.sort(key = lambda x : (x.upper(), -ord(x)))

print(" ".join(map(str, c)))
