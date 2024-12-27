import sys
sys.setrecursionlimit(3000)
n=int(input())
l=list(map(int,input().split()))
res=0
def dfs(i,h,k):
    global res
    if i==n+1:
        res=max(res,k)
        return
    else:
        if l[i-1]>=0:
            dfs(i+1,h+l[i-1],k+1)
        elif l[i-1]+h>=0:
            dfs(i+1,h+l[i-1],k+1)
            dfs(i+1,h,k)
        else:
            dfs(i+1,h,k)
dfs(1,0,0)
print(res)