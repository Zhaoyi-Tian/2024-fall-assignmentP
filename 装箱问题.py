def put(a):
    n=a[5]+a[4]+a[3]
    b2=5*a[3]
    if a[2]%4==0:
        n+=a[2]//4
    elif a[2]%4==1:
        n+=a[2]//4+1
        b2+=5
    elif a[2]%4==2:
        n+=a[2]//4+1
        b2+=3
    else:
        n+=a[2]//4+1
        b2+=1
    while a[1]>b2:
        n+=1
        b2+=9
    b1=n*36-a[5]*36-a[4]*25-a[3]*16-a[2]*9-a[1]*4
    while a[0]>b1:
        n+=1
        b1+=36
    return n
while True:
    a=list(map(int,input().split()))
    if a==[0,0,0,0,0,0]:
        break
    else:
        print(put(a))

