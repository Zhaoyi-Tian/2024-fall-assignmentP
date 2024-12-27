from collections import deque
n=int(input())
l=[input() for _ in range(n)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]
def find(l):
    for i in range(n):
        for j in range(n):
            if l[i][j]=='1':
                 return i,j
x,y=find(l)
q1=deque()
p1=set()
q1.append((x,y))
p1.add((x,y))
while q1:
    i,j=q1.popleft()
    for k in range(4):
        if 0 <= i + dx[k] < n and 0 <= j + dy[k] < n and (i + dx[k],j + dy[k]) not in p1:
            if l[i + dx[k]][j + dy[k]] == '1' :
                q1.append((i + dx[k],j + dy[k]))
                p1.add((i + dx[k],j + dy[k]))
res=float('inf')
p = set()
q=deque()
for (x,y) in p1:
    q.append((x,y,0))
    p.add((x, y))
while q:
        i,j,s=q.popleft()
        for k in range(4):
            if 0 <= i + dx[k] < n and 0 <= j + dy[k] < n and (i + dx[k],j + dy[k]) not in p:
                if l[i + dx[k]][j + dy[k]] == '1'  and (i + dx[k], j + dy[k])  in p1:
                    q.append((i + dx[k],j + dy[k],s))
                    p.add((i + dx[k], j + dy[k]))
                elif l[i + dx[k]][j + dy[k]] == '0':
                    q.append((i + dx[k], j + dy[k], s+1))
                    p.add((i + dx[k], j + dy[k]))
                elif l[i + dx[k]][j + dy[k]] == '1' and (i + dx[k], j + dy[k]) not in p1:
                    res=min(res,s)
print(res)