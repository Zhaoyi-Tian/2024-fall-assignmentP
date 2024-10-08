n,w=map(int,input().split())
c=0
d=0.0
A=[]
B=[]
C=[]
for i in range(n):
    a,b=map(int,input().split())
    e=a/b
    A.append(a)
    B.append(b)
    C.append(e)
def find_max(c):
    a=max(c)
    return [i for i,x in enumerate(c) if x==a]
while w>c and C :
        h=find_max(C)
        i=h[0]
        if c+B[i]<=w:
            c+=B[i]
            d+=A[i]
            A.pop(i)
            B.pop(i)
            C.pop(i)
        else:
            d+=(w-c)*C[i]
            c=w
            break
print(round(d,1))




