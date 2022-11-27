import sys
input = sys.stdin.readline
t = int(input())
array = [list(input()) for _ in range(t)]


def sol(array):
    stack=[]
    for i in range(len(array)):
        if array[i]=="(":
            stack.append("(")
        else:
            if len(stack)==0:
                return "NO"
            else:
                stack.pop()

    if len(stack)==0:
        return "YES"
    else:
        return "NO"


for i in range(t):
    print(sol(array[i]))

