a=[]
for i in range(5):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(5):
    if 1 in a[i]:
        x=i
    else:
        continue
y=a[x].index(1)
print(abs(x-2)+abs(y-2))
