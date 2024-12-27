n=8
ind=1
used=[[0 for _ in range(20)] for _ in range(20)]
result=[]
temp=[]
def gen(n,ind,used,temp,result):
    if ind==n+1:
        result.append(temp[:])
        return
    else:
        for i in range(1,n+1):
            if used[ind][i]==0:
                for j in range(ind,9):
                    used[j][i]+=1
                    used[j][i+(j-ind)]+=1
                    used[j][i-(j-ind)]+=1
                temp.append(i)
                gen(n,ind+1,used,temp,result)
                for j in range(ind,9):
                    used[j][i]-=1
                    used[j][i+(j-ind)]-=1
                    used[j][i-(j-ind)]-=1
                temp.pop()
gen(n,ind,used,temp,result)
result.sort()
k=int(input())
for _ in range(k):
    print(''.join(map(str,result[int(input())-1])))