import sys
input = sys.stdin.readline

n = int(input())
number = [list(map(int, input().split())) for _ in range(n)]


xpoint = {} # 수직선
ypoint = {} # 수평선
def sol(number):
    for x, y in number:
        if x in xpoint:
            xpoint[x]+=1
        else:
            xpoint[x]=1

        if y in ypoint:
            ypoint[y]+=1
        else:
            ypoint[y]=1

sol(number)
xanswer = [x for x in xpoint.values() if x>1]
yanswer = [y for y in ypoint.values() if y>1]
print(len(xanswer))
print(len(yanswer))

