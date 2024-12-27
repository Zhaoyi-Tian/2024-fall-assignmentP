n=int(input())
h=list(map(int,input().split()))*2
t=h[1:]+[h[0]]
dp=[[0 for _ in range(2*n+1)] for _ in range(2*n+1)]
for len in range(2, n + 1):
    for i in range(0, 2 * n - len + 1):
        j = len + i - 1
        for k in range(i, j):
            dp[i][j] = max(dp[i][j],h[i-1]*t[k-1]*t[j-1]+dp[i][k]+dp[k+1][j])
res=0
for i in range(n):
    res=max(res,dp[i][i+n-1])
print(res)