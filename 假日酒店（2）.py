def find(n):
    hotels=[tuple(map(int,input().split())) for i in range(n)]
    hotels.sort()
    hotel=1
    min_price=hotels[0][1]
    for i,c in hotels[1:]:
        if c>=min_price:
            continue
        else:
            hotel+=1
            min_price=c
    return hotel
while True:
    n=int(input())
    if n==0:
        break
    else:
        print(find(n))


        



