n=int(input())
a=list(i+1 for i in range(n))
b=list(map(int,input().split()))
b.sort()
c=[]
d=[]
for i in b:
    if i in a:
        c.append(i)
    else:
        d.append(i)
e=[i for i in a if i not in c]
print(" ".join(map(str,e)))
print(" ".join(map(str,d)))

