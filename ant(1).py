def ant():
   length,n=map(int,input().split())
   A=[0 for i in range(n)]
   B=[0 for i in range(n)]
   C=list(map(int,input().split()))
   for i in range(n):
       if C[i]>length-C[i]:
           A[i]+=C[i]
           B[i]+=length-C[i]
       else:
           A[i]+=length-C[i]
           B[i]+=C[i]
   print(f"{max(B)}" + " " + f"{max(A)}")
n=int(input())
for i in range(n):
    ant()