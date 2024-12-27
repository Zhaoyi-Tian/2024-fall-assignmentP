n=int(input())
times=[tuple(map(int,input().split())) for _ in range(n)]
times.sort(key=lambda x:(x[1],-x[0]))
count=1
end=times[0][1]
for time in times:
    if time[0]>end:
        count+=1
        end=time[1]
print(count)

