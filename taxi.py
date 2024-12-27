from math import ceil
n=int(input())
l={1:0,2:0,3:0,4:0}
for i in map(int,input().split()):
    l[i]+=1
a=l[1]
b=l[2]
c=l[3]
d=l[4]
if b%2==0:
    k=d+c+b//2
    if a>c:
        k+=ceil((a-c)/4)
else:
    k=d+c+b//2+1
    if a>c+2:
        k+=ceil((a-c-2)/4)
print(k)