n=int(input())
l=[0 for i in range(n+1)]
a=0
for i in range(1,n+1):
    if n*2%i==0:
        l[i]=1
l=[i for i in range(1,n+1) if l[i]==1]
l.reverse()
for i in l:
    lef=0.5*(i-2*n//i+1)
    rig=0.5*(i+2*n//i-1)
    if int(lef)==lef and lef!=rig and lef>0:
        l=list(range(int(lef),int(rig+1)))
        print('+'.join(map(str,l))+f'={n}')
        a+=1
if a==0:
    print('None')
