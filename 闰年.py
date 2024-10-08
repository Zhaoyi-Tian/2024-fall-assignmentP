def run(a):
    if a%4!=0:
        return "N"
    elif (a%100==0  and a%400!=0) or a%3200==0:
        return "N"
    else:
        return "Y"
a=int(input())
print(run(a))