x=int(input())
while x!=1:
    if x%2==0:
        y=x//2
        print(f"{x}/2={y}")
        x=y
    else:
        y=x*3+1
        print(f"{x}*3+1={y}")
        x=y
