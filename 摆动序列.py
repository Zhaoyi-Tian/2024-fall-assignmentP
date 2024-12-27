n=int(input())
l=list(map(int,input().split()))
dp=[[0,0] for _ in range(n)]
dp[0][0]=1
dp[0][1]=1
for i in range(n):
    for j in range(0,i):
        if l[i]-l[j]>0:
            dp[i][0]=max(dp[i][0],dp[j][1]+1)
        elif l[i]-l[j]<0:
            dp[i][1]=max(dp[i][1],dp[j][0]+1)
m=0
for i in range(0,n):
    if m<max(dp[i][0],dp[i][1]):
        m=max(dp[i][0],dp[i][1])
print(m)