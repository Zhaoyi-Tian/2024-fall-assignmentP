def generate(n,idx,used,temp,result):
    if idx==n+1:
        result.append(temp[:])
        return
    for i in range(1,n+1):
        if not used[i]:
            temp.append(i)
            used[i]=True
            generate(n,idx+1,used,temp,result)
            used[i] = False
            temp.pop()
n=int(input())
used=[False for _ in range(n+1)]
temp=[]
result=[]
generate(n,1,used,temp,result)
result.sort()
for i in result:
    print(' '.join(map(str,i)))


