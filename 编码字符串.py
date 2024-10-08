e=input().lower()
t=e[0]
s=[]
n=1
for i in range(1,len(e)):
    if e[i-1]==e[i]:
        n+=1
        t=e[i]
    else:
        s.append(f"({t},{n})")
        n=1
        t=e[i]
s.append(f"({t},{n})")
print(''.join(s))


