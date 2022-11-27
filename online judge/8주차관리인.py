import sys
input = sys.stdin.readline

n, m = map(int, input().split())
carorder = [list(map(int, input().split())) for _ in range(m)]

def sol(carorder):
    stack = []
    mycar = [i+1 for i in range(n)]
    parking=[]
    index=0
    while len(mycar):
        current = mycar.pop(0)
        stack.append(current)
        while len(stack) and stack[-1]==carorder[index]:
            parking.append(stack.pop())
            index+=1
    while len(stack):
        parking.append(stack.pop())
    return parking

def answer(a, b):
    if a==b:
        return 'yes'
    else:
        return 'no'

for i in range(m):
    print(answer(sol(carorder[i]), carorder[i]))

    