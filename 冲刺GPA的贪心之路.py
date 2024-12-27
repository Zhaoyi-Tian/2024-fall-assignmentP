h=2*int(input())
m=int(input())
h-=m*0.5
l=[]
for i in range(m):
    a,b=map(float,input().split())
    l.append((a*b,a))
res=0.0
l.sort(key=lambda x:-x[0])
for i in range(m):
    if h<=0:
        break
    if l[i][1]*h<=5:
        res+=l[i][0]*h
        h=0
    else:
        res+=5*l[i][0]/l[i][1]
        h-=5/l[i][1]
print(f'{res:.1f}')