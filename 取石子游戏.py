def find(a,b):
    a,b=max(a,b),min(a,b)
    while True:
        if a==b:
            return 'win'
        if a/b>=2 or a==b:
            return 'win'
        else:
            a-=b
            if a==b:
                return 'lose'
            elif b/a>=2 :
                return 'lose'
            else:
                b-=a
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    print(find(a,b))
