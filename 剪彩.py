from math import log2
def find(n,l):
    dp=[[0,0,0] for i in range(n+1)]
    dp[0] = [1, 1, 1]
    for i in range(1,n+1):
        for j in range(3):
            if i>=l[j]:
                dp[i][j]=max(dp[i-l[j]])*2
    print(int(log2(max(dp[n]))))
n,a,b,c=map(int,input().split())
l=[a,b,c]
find(n,l)
