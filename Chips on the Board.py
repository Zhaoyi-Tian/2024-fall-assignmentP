def find():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    k1=sum(a)+min(b)*n
    k2=sum(b)+min(a)*n
    return min(k1,k2)
n=int(input())
for i in range(n):
    print(find())



