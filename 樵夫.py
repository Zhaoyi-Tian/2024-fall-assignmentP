n=int(input())
trees=[tuple(map(int,input().split())) for i in range(n)]
def cut(n,trees):
    if n==1:
        return 0
    if n==2:
        return 1
    dp=[[0,0] for i in range(n)]
    dp[0][0]=1
    if trees[0][0]+trees[0][1]<trees[1][0]:
        dp[0][1]=1
    for i in range(1,n-1):
        if trees[i][0]-trees[i][1]>trees[i-1][0]:
            dpa=dp[i-1][0]+1
        else:
            dpa=dp[i-1][0]
        if trees[i][0]-trees[i][1]>trees[i-1][0]+trees[i-1][1]:
            dpb=dp[i-1][1]+1
        else:
            dpb=dp[i-1][1]
        dp[i][0]=max(dpa,dpb)
        if trees[i][0]+trees[i][1]<trees[i+1][0]:
            dp[i][1]=max(dp[i-1][0],dp[i-1][1])+1
        else:
            dp[i][1]=max(dp[i-1][0],dp[i-1][1])
    return max(dp[n-2][0],dp[n-2][1])
print(cut(n,trees)+1)


