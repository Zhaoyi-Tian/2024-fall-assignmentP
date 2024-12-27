n,c=map(int,input().split())
l=sorted([int(input()) for i in range(n)])
def ok(d,n,c):
    c-=1
    last=l[0]
    for i in range(1,n):
        if l[i]-last>=d:
            c-=1
            last=l[i]
    if c<=0:
        return True
    else:
        return False
def find(n,c):
    left=0
    right=l[n-1]-l[0]
    while left<=right-1:
        mid=(left+right)//2
        if ok(mid,n,c):
            right=mid
        else:
            left=mid
    return mid
print(find(n,c))

