from math import gcd
n=int(input())
result=set()
def gcd_three(a,b,c):
    return gcd(gcd(a,b),c)
def y(a,n):
    global result
    for b in range(1,n):
        c=n-b-a
        if a>b>c>0:
          d=gcd_three(a,b,c)
          result.add(d)
for a in range(1,n-1):
    y(a,n)
print(max(result))
