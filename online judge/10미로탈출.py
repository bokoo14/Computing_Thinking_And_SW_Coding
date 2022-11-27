import sys
input=sys.stdin.readline

n, m = map(int, input().split())
maze=[list(map(int, input().split())) for _ in range(n)]

# dp table
dp=[[0]*(m)]*(n)

def sol(n, m):
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                dp[i][j]=maze[i][j]
            elif i==0:
                dp[i][j]=maze[i][j]+dp[i][j-1]
            elif j==0:
                dp[i][j]=maze[i][j]+dp[i-1][j]
            else:
                dp[i][j]=maze[i][j]+min(dp[i-1][j], dp[i][j-1])

sol(n, m)
#print(dp)
print(dp[n-1][m-1])                
