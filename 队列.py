n=int(input())
l=list(map(int,input().split()))
l.sort()
sum=0
n=0
for i in l:
    if i>=sum:
        sum+=i
        n+=1
    else:
        continue
print(n)
