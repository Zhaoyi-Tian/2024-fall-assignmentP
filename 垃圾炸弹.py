d=int(input())
n=int(input())
l=[[0 for _ in range(1025)] for _ in range(1025)]
for i in range(n):
            x, y, k = map(int, input().split())
            for i in range(max(x - d, 0), min(x + d + 1, 1025)):
                for j in range(max(y - d, 0), min(y + d + 1, 1025)):
                    l[i][j] += k
m=0
count=0
for i in range(1025):
    for j in range(1025):
        if l[i][j]>m:
            m=l[i][j]
            count=1
        elif l[i][j]==m:
            count+=1
print(f'{count} {m}')


