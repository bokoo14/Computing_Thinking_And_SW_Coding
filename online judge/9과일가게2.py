import sys
input = sys.stdin.readline

n = int(input())
fruit = [input().strip() for _ in range(n)]

sale = {}
def sol(fruit, n):
    for i in fruit:
        if i in sale:
            sale[i]+=1
        else:
            sale[i]=1

sol(fruit, n)
answer = sorted(sale.items(), key = lambda x: (-x[1], [x[0]]))

for i in range(len(answer)):
    print(answer[i][1], answer[i][0])

