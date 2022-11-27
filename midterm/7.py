import sys
input = sys.stdin.readline


x = [92255, 63361, 15009, 11417, 78633, 13816]
x.sort()
print(x)
cnt = 0
def sol(first, last, i):
    global cnt
    cnt+=1
    if first>last:
        return 
    mid = (first+last)//2
    if x[mid] == i:
        return 0

    if x[mid]<i:
        return sol(mid+1, last, i)
    else:
        return sol(first, mid-1, i)

answer =0
for i in x:
    # print(i)
    answer=sol(0,len(x)-1, i)
    print(cnt)
    answer+=cnt

print(cnt)
print(answer)