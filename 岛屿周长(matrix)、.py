n,m=map(int,input().split())
a=0
l=[[0 for _ in range(m+2)] for _ in range(n+2)]
for i in range(1,n+1):
    l[i][1:m+1]=list(map(int,input().split()))
for i in range(1,n+1):
    for j in range(1,m+1):
        if l[i][j]==1:
            if l[i+1][j]==1 or l[i-1][j]==1 or l[i][j+1]==1 or l[i][j-1]==1:
                if l[i][j-1]==0:
                    a+=1
                if l[i][j+1]==0:
                    a+=1
                if l[i-1][j]==0:
                    a+=1
                if l[i+1][j]==0:
                    a+=1
print(a)