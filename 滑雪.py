from functools import lru_cache
dx=[0,0,1,-1]
dy=[1,-1,0,0]
r,c=map(int,input().split())
l=[list(map(int,input().split())) for j in range(r)]
res=1
@lru_cache(maxsize=None)
def dfs(x,y):
    max_length = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and l[nx][ny] < l[x][y]:
            max_length = max(max_length, 1 + dfs(nx, ny))
    return max_length
for x in range(r):
    for y in range(c):
        res=max(res,dfs(x,y))
print(res)
