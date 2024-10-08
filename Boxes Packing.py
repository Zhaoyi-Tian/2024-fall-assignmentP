n=int(input())
l=list(map(int,input().split()))
l.sort()
k=0
def find():
    global l
    a=0
    for i in l:
        if i>a:
            a=i
            l.remove(i)
while l:
    find()
    k+=1
print(k)
