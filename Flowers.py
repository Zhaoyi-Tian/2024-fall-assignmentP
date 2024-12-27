t,k=map(int,input().split())
dp=[0 for i in range(10**5+2)]
for i in range(1,k):
    dp[i]=1
dp[k]=2
for i in range(k+1,10**5+2):
    dp[i]=(dp[i-k]+dp[i-1])%1000000007
s=[0 for _ in range(10**5+2)]
for i in range(1,10**5+2):
    s[i]=(dp[i]+s[i-1])%1000000007
for i in range(t):
    a,b=map(int,input().split())
    print((s[b]-s[a-1])%1000000007 )
