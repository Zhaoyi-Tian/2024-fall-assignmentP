b=int(input())
boys=list(map(int,input().split()))
g=int(input())
girls=list(map(int,input().split()))
boys.sort()
girls.sort()
def find(a,b):
    if a==b or a==b+1 or a==b-1:
        return True
    else:
        return False
i=0
j=0
n=0
while i<len(boys) and j<len(girls):
    if find(boys[i],girls[j]):
        n+=1
        i+=1
        j+=1
    elif boys[i]>girls[j]:
        j+=1
    elif boys[i]<girls[j]:
        i+=1
print(n)




