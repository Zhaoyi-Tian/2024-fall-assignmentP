a=list(0 for i in range(20))
a[0]=1
a[1]=1
for i in range(2,20):
    a[i]=a[i-1]+a[i-2]
n=int(input())
for _ in range(n):
    i=int(input())
    print(a[i-1])
