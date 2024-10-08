n=int(input())
l=[]
for i in range(2,n+1):
    for d in range(2,i+1):
        for c in range(2,d+1):
            for b in range(2,c+1):
                if i**3==b**3+c**3+d**3:
                    l.append((i,b,c,d))
l.sort()
for i,b,c,d in l:
    print(f"Cube = {i}, Triple = ({b},{c},{d})")
