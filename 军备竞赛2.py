n=int(input())
l=list(map(int,input().split()))
l.sort()
b=len(l)
a=0
if n>=l[0]:
    k=0
    while True:
        if n>=l[k] :
            n-=l[k]
            k+=1
            a+=1
        else:
            if k<b-1:
                n+=l[-1]
                l.pop(-1)
                b-=1
                a-=1
        if k==b-1:
            break
if n>=l[-1]:
    a+=1
print(a)