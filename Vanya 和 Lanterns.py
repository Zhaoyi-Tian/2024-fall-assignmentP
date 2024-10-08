n,l=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
d=[r[0]]
for i in range(1,n):
    d.append((r[i]-r[i-1])/2)
d.append(l-r[n-1])
print(round(max(d),10))
