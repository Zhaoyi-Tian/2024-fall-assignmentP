def find(n,t):
    a=n%t
    return {a+i*t for i in range(1000)}
def k():
    p,e,i,d=map(int,input().split())
    if d<0:
        return -1
    else:
        p_1=find(p,23)
        e_1=find(e,28)
        i_1=find(i,33)
        l=[i-d for i in p_1 if i in e_1 and i in i_1]
        l=[i for i in l if i>=0]
        return min(l)
n=0
while True:
   n+=1
   c=k()
   if c==-1:
       break
   else:
    if c==0:
        print(f'Case {n}: the next triple peak occurs in 21252 days.')
    else:
        print(f'Case {n}: the next triple peak occurs in {c} days.')

