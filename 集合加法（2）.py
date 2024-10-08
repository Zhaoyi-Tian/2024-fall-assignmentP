def find():
    n=0
    s=int(input())
    a=int(input())
    A=list(map(int,input().split()))
    b=int(input())
    B=list(map(int,input().split()))
    for i in range(a):
        C=B[:]
        while s-A[i] in C:
            n+=1
            C.remove(s-A[i])
    print(n)
n=int(input())
for i in range(n):
    find()
