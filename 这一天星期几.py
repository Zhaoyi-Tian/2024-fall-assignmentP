from math import floor
l={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
def find(x):
    c=int(x[0:2])
    y=int(x[2:4])
    m=int(x[4:6])
    d=int(x[6:8])
    if m==1 or m==2:
        if y==0:
            c-=1
            y=99
        else:
            y-=1
        m+=12

    w=(y+floor(y/4)+floor(c/4)-2*c+floor(26*(m+1)/10)+d-1)%7
    print(l[w])
n=int(input())
for i in range(n):
    find(input())


