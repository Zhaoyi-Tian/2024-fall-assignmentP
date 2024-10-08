n=int(input())
l=[int(input()) for i in range(n)]
m=max(l)
a=[0 for i in range(m)]
a[0]=1
a[1]=2
for i in range(2,m):
    a[i]=2*a[i-1]+a[i-2]
for i in l:
    print(a[i-1])

