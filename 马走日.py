d=[[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
def dfs(x,y,n,m):
    visited[y][x]=1
    if visited==l:
        return 1
    a=0
    for i in range(8):
        if 0<=x+d[i][1]<n and 0<=y+d[i][0]<m:
            if visited[y+d[i][0]][x+d[i][1]]==0:
                a+=dfs(x+d[i][1],y+d[i][0],n,m)
                visited[y+d[i][0]][x+d[i][1]]=0
    return a
k=int(input())
for i in range(k):
    n,m,x,y=map(int,input().split())
    visited=[[0 for _ in range(n)]for j in range(m)]
    l=[[1 for _ in range(n)]for j in range(m)]
    print(dfs(x,y,n,m))
