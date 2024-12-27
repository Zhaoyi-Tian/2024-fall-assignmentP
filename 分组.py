from collections import defaultdict
import heapq
n=int(input())
l=list(map(int,input().split()))
d=defaultdict(int)
for i in l:
    d[i]+=1
k=[]
for num in sorted(d.keys()):
        heapq.heappush(k, [1, [num]])
res=float('inf')
while d:
    if not k:
        break
    o=heapq.heappop(k)
    if o[1][-1]+1 in d and d[o[1][-1]+1]>0:
        d[o[1][-1]+1]-=1
        o[0]+=1
        o[1].append(o[1][-1]+1)
        heapq.heappush(k,o)
    else:
        res=min(res,o[0])
print(res)
