def find(n,p,m):
    l=list(range(n))
    l_1=[]
    p-=1
    b=n
    for _ in range(n):
        c=l.pop((p+m-1)%b)
        l_1.append(c)
        p=(p+m-1)%b
        b-=1
    l_2=[i+1 for i in l_1]
    print(",".join(map(str,l_2)))
while True:
    n, p, m = map(int, input().split())
    if n==0 and m==0 and p==0:
        break
    else:
        find(n,p,m)
