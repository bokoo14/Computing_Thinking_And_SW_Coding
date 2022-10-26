import sys
input = sys.stdin.readline

n=int(input())
array=list(map(int, input().split()))

answer=[]
for i in range(len(array)):
    if (i+1)==array[i]:
        answer.append(array[i])

print(len(answer))
print(* answer)