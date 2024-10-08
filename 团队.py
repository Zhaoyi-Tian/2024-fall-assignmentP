number=0
def opinion(p):
    global number
    a=int(p[0])
    b=int(p[2])
    c=int(p[4])
    finish=a+b+c
    if finish>=2:
        number=number+1
n=int(input())
for i in range(n):
    i=input()
    opinion(i)
print(number)


