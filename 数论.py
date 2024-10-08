from math import sqrt
def y(a):
    count=0
    if a==1:
        return 0
    elif a%4==0:
        return -1
    elif a%2==0:
        count+=1
        a=a/2
    for i in range (3,int(sqrt(a))+1,2):
        if a%(i**2)==0:
            return -1
        elif a%i==0:
            count+=1
            a=a/i
    if a==1:
        return count
    if a!=1:
        count+=1
        return count
def b(a):
    if a%2==0:
        return 1
    elif a==-1:
        return 0
    else:
        return -1
print(b(y(int(input()))))



