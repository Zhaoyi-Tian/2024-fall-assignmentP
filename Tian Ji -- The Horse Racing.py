while True:
    n=int(input())
    a=0
    if n==0:
        break
    tian=sorted(list(map(int,input().split())),reverse=True)
    king=sorted(list(map(int,input().split())),reverse=True)
    while tian:
            if tian[-1] > king[-1]:
                a += 1
                tian.pop()
                king.pop()
            elif tian[0]>tian[0]:
                a+=1
                tian.pop(0)
                king.pop(0)
            else:
                if tian[-1] < king[0]:
                    a-= 1
                tian.pop()
                king.pop(0)



    print(a*200)
