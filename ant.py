def find(a,b):
    C=[min(a[i],b[i]) for i in range(len(a))]
    D=[max(a[i],b[i]) for i in range(len(a))]
    print(f"{max(C)}"+" "+f"{max(D)}")
def ant():
   length,n=map(int,input().split())
   A=list(map(int,input().split()))
   B=list(0 for i in range(n))
   for i in range(n):
       b=length-A[i]
       B.append(b)
       find(A,B)
n=int(input())
for i in range(n):
    ant()


