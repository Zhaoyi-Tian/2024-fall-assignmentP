n,m=map(int,input().split())
d=[[-1,0],[1,0],[0,1],[0,-1]]
visited=[[0 for _ in range(m)] for _ in range(n)]
visited[0][0]=1
l=[list(map(int,input().split())) for _ in range(n)]
result=[]
k=-float('inf')
def dfs(x,y,n,m,temp,p):
    global result
    global k
    if x==n-1 and y==m-1:
        if p>k:
            k=p
            result=temp[:]
    for i in range(4):
        if 0<=x+d[i][0]<n and 0<=y+d[i][1]<m:
            if visited[x+d[i][0]][y+d[i][1]]==0:
                visited[x+d[i][0]][y+d[i][1]]=1
                a=temp[:]+[[x+d[i][0]+1,y+d[i][1]+1]]
                dfs(x+d[i][0],y+d[i][1],n,m,a,p+l[x+d[i][0]][y+d[i][1]])
                visited[x+d[i][0]][y+d[i][1]]=0
dfs(0,0,n,m,[[1,1]],l[0][0])
for i in result:
    print(' '.join(map(str,i)))