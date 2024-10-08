from functools import lru_cache
@lru_cache(maxsize=None)
def c(n):
    return 2**n
def h(n):
    d=0
    e=0
    for i in range(n):
        if (i+1)%c(d)==0:
            d+=1
            e-=i+1
        else:
            e+=i+1
    print(e)
n=input()
while True:
    try:
        h(int(input()))
    except EOFError:
        break


