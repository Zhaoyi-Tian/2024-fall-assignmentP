A=[]
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if a*100+b*10+c==a**3+b**3+c**3:
                A.append(a*100+b*10+c)
print(A)