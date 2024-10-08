n=int(input())
l=map(int,input().split())
c=list(range(1,1000000))
i=1
while i<len(c):
    c=[k for k in c if k%c[i]!=0 or k==c[i]]
    i+=1
def find(i):
    return int(i**0.5)==i**0.5
def a(i):
    if not find(i) or i==1:
        return "NO"
    else:
        if i**0.5 in c:
            return "YES"
        else:
            return "NO"
for i in l:
    print(a(i))