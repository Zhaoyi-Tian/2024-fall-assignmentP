
n,m=map(int,input().split())
price=[list(input().split()) for _ in range(n)]
quan=[list(input().split()) for _ in range(m)]
la=[0 for _ in range(m)]
result=float('inf')
def dfs(i):
    global result
    if i==n+1:
        s=sum(la)
        s-=(sum(la)//300)*50
        for i2 in range(m):
            store_j = 0
            for k in quan[i2]:
                a, b = map(int, k.split('-'))
                if la[i2] >= a:
                    store_j = max(store_j, b)
            s-=store_j
        result=min(result,s)
        return
    else:
        for j in price[i-1]:
            a,b=map(int,j.split(':'))
            la[a-1]+=b
            dfs(i+1)
            la[a-1]-=b
dfs(1)
print(result)
