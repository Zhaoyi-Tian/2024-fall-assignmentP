n=int(input())
l=list(tuple(map(int,input().split())) for _ in range(n+1))
def find(a,b,c,d):
    if a*b>c*d:
        return True
    return False
for i in range(0,n):
     s=False
     for j in range(1,n-i):
         a,b=l[j]
         c,d=l[j+1]
         if find(a,b,c,d):
             l[j],l[j+1]=l[j+1],l[j]
             s=True
     if not s:
        break
m=0
k,p=l[0]
for i in range(1,n+1):
    m=max(m,k//l[i][1])
    k*=l[i][0]
print(m)
