A=[]
B=[]
for a in range(0,11):
    for b in range(0,10):
        for c in range(0,10):
            if a*100+b*10+c==a**3+b**3+c**3:
                A.append(a*100+b*10+c)
A.sort()
a,b=map(int,input().split())
for i in A:
    if a<=i<=b:
        B.append(i)
if B:
    print(" ".join(map(str,B)))
else:
    print("NO")

