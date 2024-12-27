l=list(input())
while len(l)!=1:
    a=[i for i,_ in enumerate(l) if _=='[']
    b = [i for i, _ in enumerate(l) if _ == ']']

