def solve(n):
    if n%4==0:
        a=n/4
        b=n/2
    elif n%2==0:
        a=n//4+1
        b=n//2
    else:
        a=0
        b=0
    return(str(int(a))+" "+str(int(b)))
n=int(input())
print(solve(n))