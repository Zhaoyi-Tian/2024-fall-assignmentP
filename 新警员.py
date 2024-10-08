n=int(input())
l=list(map(int,input().split()))
a=0
b=0
for i in l:
    if i>0:
        b+=i
    else:
        if b==0:
            a+=1
        else:
            b-=1
print(a)
