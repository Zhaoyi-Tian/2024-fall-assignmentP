from collections import deque
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs(x1,y1,x2,y2):
    global n
    inq=set()
    inq.add((x1,y1,x2,y2))
    q=deque()
    q.append((x1,y1,x2,y2))
    while q:
        x1,y1,x2,y2=q.popleft()
        for i in range(4):
            nx1=x1+dx[i]
            ny1=y1+dy[i]
            nx2=x2+dx[i]
            ny2=y2+dy[i]
            if (nx1,ny1,nx2,ny2) in inq or (nx2,ny2,nx1,ny1) in inq:
                continue
            else:
                if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n:
                    if l[nx1][ny1]!="1" and l[nx2][ny2]!="1":
                        q.append((nx1,ny1,nx2,ny2))
                        inq.add((nx1,ny1,nx2,ny2))
                    if (l[nx1][ny1]=="9" or l[nx2][ny2]=="9") and l[nx1][ny1]!="1" and l[nx2][ny2]!="1":
                        return 'yes'
    return 'no'
n=int(input())
l=[list(input().split()) for _ in range(n)]
k=[]
for i in range(n):
    for j in range(n):
        if l[i][j]=="5":
            k.append(i)
            k.append(j)
print(bfs(k[0],k[1],k[2],k[3]))