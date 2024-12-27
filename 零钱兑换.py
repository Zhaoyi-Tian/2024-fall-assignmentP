n,m=map(int,input().split())
l=list(map(int,input().split()))
dp=[float('inf')]*(m+1)
dp[0]=0
for i in range(1,m+1):
    dp[i]=min(dp[i-l[j]] for j in range(n))+1
print(dp[m])