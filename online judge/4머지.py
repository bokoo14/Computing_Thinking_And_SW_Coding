import sys
input = sys.stdin.readline

s, t = input().split()

s= sorted(list(s.upper()))
t = sorted(list(t.lower()))

c = s+t
c.sort(key = lambda x : (x.upper(), -ord(x)))

print(" ".join(map(str, c)))
