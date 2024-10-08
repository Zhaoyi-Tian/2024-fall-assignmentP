n=int(input())
li=list(map(int,input().split()))
li1=sorted(li)
def first(l,r):
    return sum(li[l-1:r])
def second(l,r):
    return sum(li1[l-1:r])
q=int(input())
for i in range(q):
    type,l,r=map(int,input().split())
    if type==1:
        print(first(l,r))
    if type==2:
        print(second(l,r))