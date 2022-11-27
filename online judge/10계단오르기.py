import sys
input=sys.stdin.readline

n = int(input())
step=list(map(int, input().split()))

dp=[0]*(n)
dp[0]=step[0]
dp[1]=max(step[0]+step[1], step[1])
for i in range(2, n):
    dp[i]=step[i]+max(dp[i-1], dp[i-2])


print(dp[n-1])

