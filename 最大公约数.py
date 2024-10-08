from math import gcd
while True:
    try:
        a,b=map(int,input().split())
        d=gcd(a,b)
        print(d)
    except EOFError:
        break