def kill(n,m,b):
    l=list(tuple(map(int,input().split())) for _ in range(n))
    tl=sorted(list({t for (t,x) in l}))
    for t in tl:
        nl=[]
        for (y,x) in l:
            if y==t:
                nl.append(x)
        nl.sort()
        k=len(nl)
        if k<=m:
            b-=sum(nl)
        else:
            b-=sum(nl[k-m:k])
        if b<=0:
            return t
    if b>0:
        return 'alive'
n=int(input())
for _ in range(n):
    a,b,c=map(int,input().split())
    print(kill(a,b,c))