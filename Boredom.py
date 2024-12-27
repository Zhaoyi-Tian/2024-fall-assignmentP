n=int(input())
l=sorted(list(map(int,input().split())))
d=dict()
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
dp=[0 for _ in range(6)]
for i in range(1,7):
    if i in d:
        dp[i%6]=max(dp[i%6-2]+i*d[i],dp[i%6-1])
    else:
        dp[i%6]=dp[i%6-1]
for i in range(7,100001):
    if i in d:
        dp[i%6]=max(dp[i%6-2]+i*d[i],dp[i%6-1])
    else:
        dp[i%6]=dp[i%6-1]
print(max(dp))
