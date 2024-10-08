n=int(input())
if n%2!=0 or n<6:
    print("Error!")
else:
    l=[_ for _ in range(2,n)]
    k=0
    while k<len(l):
        l=[x for x in l if x==l[k] or x%l[k]!=0]
        k+=1
    for p in l:
        if p>n-p:
            break
        if n-p in l:
            print(f"{n}={p}+{n-p}")


