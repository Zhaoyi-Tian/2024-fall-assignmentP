from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def walk(r,c,k):
    l=[input() for _ in range(r)]
    for I in range(r):
        for J in range(c):
            if l[I][J] == 'S':
                A,B=I,J
    q=deque([(A,B,0)])
    visited = set()
    visited.add((A,B,0))
    while q:
        a,b,t=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<r and 0<=ny<c :
                if (nx, ny,(t+1)%k) not in visited:
                    if l[nx][ny] == 'E':
                        return t+1
                    if (t+1)%k==0:
                        q.append((nx,ny,t+1))
                        visited.add((nx,ny,(t+1)%k))
                    else:
                        if l[nx][ny] != '#':
                            q.append((nx,ny,t+1))
                            visited.add((nx, ny, (t + 1) % k))
    return 0
T=int(input())
for i in range(T):
    r,c,k=map(int,input().split())
    p=walk(r,c,k)
    if p==0:
        print("Oop!")
    else:
        print(p)

