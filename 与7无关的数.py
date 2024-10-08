result=0
def math(a):
    if a%7==0 or "7" in str(a):
        return 0
    else:
        return a**2
n=int(input())
for a in range(1,n+1):
    result+=math(a)
print(result)