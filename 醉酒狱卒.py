def find(n):
    a=0
    for i in range(1,n+1):
        b=0
        for j in range(1,n+1):
            if i%j==0:
                b+=1
        if b%2==1:
            a+=1
    print(a)
n=int(input())
for i in range(n):
    find(int(input()))
