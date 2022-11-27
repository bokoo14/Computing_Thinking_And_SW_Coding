import sys
input = sys.stdin.readline

n = int(input())
array = sorted(list(input().strip()) for _ in range(n))
#print(array)

answer = {}
def check(word):
    tmp = ''.join(sorted(word))
    if tmp in answer:
        answer[tmp].append(''.join(word))
    else:
        answer[tmp] = [''.join(word)]


for i in range(n):
    check(array[i])

answer = list(answer.values())

for i in range(len(answer)):
    print(' '.join(answer[i]))