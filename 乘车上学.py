import math
def time(a,b):
    if b>=0:
        return 4.5/a*3600+b
    else:
        return 10000000000000000000
def find(n):
    A=[]
    for i in range(n):
        a,b=map(int,input().split())
        A.append(time(a,b))
    m=min(A)
    print(math.ceil(m))
while True:
    n=int(input())
    if n!=0:
        find(n)
    else:
        break