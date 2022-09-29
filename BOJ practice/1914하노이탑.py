import sys
input = sys.stdin.readline

n=int(input())
cnt=0
def hanoi(N, start, end, middle):
    global cnt
    if N==0:
        return 
    else: 
        hanoi(N-1, start, middle, end)
        print(start, middle)
        hanoi(N-1, middle, end, start)
        cnt+=1

print(cnt)
hanoi(n, 1, 2, 3)


