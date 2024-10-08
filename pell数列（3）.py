def a(n):
    b=1
    c=2
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for _ in range(n-2):
            d=(2*c+b)%32767
            b=c%32767
            c=d%32767
        return d
n=int(input())
for _ in range(n):
    print(a(int(input())))

