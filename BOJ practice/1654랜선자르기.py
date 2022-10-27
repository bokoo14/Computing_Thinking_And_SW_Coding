import sys
input = sys.stdin.readline
'''
k, n = map(int, input().split())
wire = [int(input()) for _ in range(k)]

#이진탐색 알고리즘 <cut할 랜선의 최대 길이 선택>
def wire_cut(start, end):
    if start>end:
        return end
    
    cut=(start+end)//2
    cnt=0 #자른 랜선의 수 

    for i in range(0, k): #자른 랜선의 수
        cnt+=wire[i]//cut

    if cnt>=n:
        return wire_cut(cut+1, end)
    else:
        return wire_cut(start, cut-1)


print(wire_cut(1, max(wire)))




# 2번째 
k, m = map(int, input().split()) # 가지고 있는 랜선의 개수, 필요한 랜선의 개수
line = [0]*k
for i in range(k):
    line[i] = int(input())

def sol(k, m, first, last):
    if first>last:
        return last

    mid = (first+last)//2
    sum = 0
    for j in range(k): # 랜선 자르기. 남은건 다 버리기
        sum+=line[j]//mid 

   
    if sum < m: 
        return sol(k, m, first, mid-1)
    else:
        return sol(k, m ,mid+1, last)

print(sol(k, m, 1, max(line)))
'''
# while 문으로 풀이
def count(L, mid):
    cnt = 0
    for i in range(len(L)):
        cnt += L[i]//mid
    return cnt

def solve(L, N):
    low, high = 1, max(L)
    while low <=high:
        mid = (low + high)//2
        cnt = count(L, mid)
        
        
        if cnt < N:
            high = mid-1
        else:
            low = mid +1

    return high

K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]
print(solve(L, N))
