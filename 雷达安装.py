from math import sqrt
def find(n,d):
    l=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        x=l[i][0]
        y=l[i][1]
        if y>d:
            return -1
        l[i][0]=x-sqrt(d**2-y**2)
        l[i][1]=x+sqrt(d**2-y**2)
    l.sort(key=lambda x: x[0])
    p=1
    m=min(l[i][1] for i in range(n))
    k=0
    while True:
        if l[k][0]<=m:
            m=min(m,l[k][1])
            k+=1
        else:
            if k<=n-1:
                m = l[k][1]
            k+=1
            p+=1
        if k>=n:
            break
    return p
a=0
while True:
    a+=1
    n,d=map(int,input().split())
    if n==0 and d==0:
        break
    print(f'Case {a}: {find(n,d)}')
    h=input()



