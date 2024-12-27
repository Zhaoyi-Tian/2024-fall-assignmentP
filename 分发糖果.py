ratings=input()
ratings = ratings.strip('[]').split(',')
ratings=[int(x) for x in ratings]
ratings=[0]+ratings
n=len(ratings)-1
dp=[[float('inf') for _ in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    dp[1][i]=i
for i in range(2,n+1):
    for j in range(1,n+1):
        if ratings[i]<ratings[i-1]:
            if j<n:
                dp[i][j]=min(dp[i-1][j+1:n+1])+j
        elif ratings[i]<ratings[i-1]:
            if j>1:
                dp[i][j]=min(dp[i-1][1:j])+j
        else:
            dp[i][j]=min(dp[i-1])+j

print(min(dp[n]))


