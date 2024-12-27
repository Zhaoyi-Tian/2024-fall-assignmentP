n=int(input())
h=map(int,input().split())
l=[]
k=0
a=0
for i in h:
    k+=1
    l.append((k,i))
l.sort(key=lambda x:x[1])
h=[x for (x,y) in l]
print(' '.join(map(str,h)))
p=0
for (x,y) in l:
    p+=1
    a+=y*(n-p)
print(f'{a/n:.2f}')
