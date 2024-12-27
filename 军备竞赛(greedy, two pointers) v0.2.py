
n=int(input())
l=list(map(int,input().split()))
l.sort()
b=len(l)
a=0
if n<l[0]:
    print('0')
else:
    k=0
    while True:
        if n>=l[k]:
            n-=l[k]
            k+=1
            a+=1
        else:
            if k<b-1:
                if n+l[-1]<l[k]+l[k+1]:
                    break
                else:
                    n=l[-1]+l[k+1]+l[k]+n
                    b-=1
                    l.remove(l[-1])
                    a+=1
            else:
                break
    print(a)



