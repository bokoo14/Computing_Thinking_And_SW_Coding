import sys
input = sys.stdin.readline

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
