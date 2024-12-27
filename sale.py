n,m=map(int,input().split())
l=list(map(int,input().split()))
l=[-i for i in l if i<0]
a=len(l)
l.sort(reverse=True)
if m>=a:
    v=sum(l)
else:
    v=sum(l[0:m])
print(v)