n=int(input())
m=[[0 for _ in range(n)] for _ in range(n)]
left,right=0,n-1
top,bottom=0,n-1
k=1
while k<=n**2:
    for i in range(left,right+1):
        m[top][i]=k
        k+=1
    top+=1
    for i in range(top,bottom+1):
        m[i][right]=k
        k+=1
    right-=1
    for i in range(right,left-1,-1):
        m[bottom][i]=k
        k+=1
    bottom-=1
    for i in range(bottom,top-1,-1):
        m[i][left]=k
        k+=1
    left+=1
for i in range(n):
    print(' '.join(map(str,m[i])))
