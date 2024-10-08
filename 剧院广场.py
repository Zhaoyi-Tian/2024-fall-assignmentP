n,m,a=map(int,input().split())
def g(n):
    if n%a!=0:
        return n//a+1
    else:
        return n//a
print(int(g(n)*g(m)))