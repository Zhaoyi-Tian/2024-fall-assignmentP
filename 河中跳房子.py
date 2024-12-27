l,n,m=map(int,input().split())
st=list(int(input()) for _ in range(n))+[l]
def find(s):
    i=0
    p=0
    for j in range(n+1):
        if st[j]-p<s:
            i+=1
        else:
            p=st[j]
        if i>m:
            return False
    return True
left=0
right=l+1
while left<right:
    mid=(left+right)//2
    if find(mid):
        left=mid+1
        ans=mid
    else:
        right=mid
print(ans)


