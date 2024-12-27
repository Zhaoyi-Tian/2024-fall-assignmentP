m,n,p,q=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
k=[list(map(int,input().split())) for i in range(p)]
h=[[0 for _ in range(n+1-q)] for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        for e in range(p):
            for w in range(q):
                h[i][j]+=k[e][w]*l[i+e][j+w]
for i in range(m+1-p):
    print(' '.join(map(str,h[i])))