n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
i=0
while sum(l[0:i])<=sum(l[i:n]):
    i+=1
print(i)