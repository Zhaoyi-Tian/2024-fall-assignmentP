def find(n):
    C=[0 for i in range(n)]
    D=[0 for i in range(n)]
    a=0
    for i in range(n):
        d,c=map(int,input().split())
        C[i]=c
        D[i]=d
    for i in range(n):
        b=0
        for j in range(n):
            if D[j]>D[i] and C[j]<C[i]:
                b+=1
            elif D[j]<=D[i] and C[j]>=C[i]:
                b+=1
            else:
                break
        if b==n:
            a+=1
    print(a)
while True:
    n=int(input())
    if n==0:
        break
    else:
        find(n)





