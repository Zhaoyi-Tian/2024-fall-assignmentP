n,m=map(int,input().split())
def j(n):
    k=1
    for i in range(1,n+1):
        k*=i
    return k
print(j(m+n-2)//(j(n-1)*j(m-1)))