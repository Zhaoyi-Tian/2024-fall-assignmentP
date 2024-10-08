def find(n,m):
    a=list(range(1,n+1))
    b=n
    e=0
    for _ in range(n-1):
        d=(m-1+e)%b
        a.pop(d)
        e=d
        b-=1
    for i in a:
        print(i)
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    else:
        find(n,m)

