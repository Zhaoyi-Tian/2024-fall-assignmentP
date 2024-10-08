def find():
    n=0
    s=int(input())
    a=int(input())
    A=list(map(int,input().split()))
    b=int(input())
    B=list(map(int,input().split()))
    for i in range(a):
        for j in range(b):
            if A[i]+B[j]==s:
                n+=1
    print(n)
n=int(input())
for i in range(n):
    find()

