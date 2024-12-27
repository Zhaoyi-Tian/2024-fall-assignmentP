n=int(input())
l=[0 for _ in range(n)]
l[0]=1
for i in range(1,n):
    l[i]=2*l[i-1]+1
print(l[n-1])
def move(n,from_,to_,help_):
    if n==0:
        return
    move(n-1,from_,help_,to_)
    print(f'{from_}->{to_}')
    move(n-1,help_,to_,from_)
move(n,'A','C','B')
