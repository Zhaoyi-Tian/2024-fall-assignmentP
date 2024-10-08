M,N=map(int,input().split())
def d(M,N):
    if M%2==0 or N%2==0:
        n=M*N/2
    else:
        n=(M*N-1)/2
    return int(n)
print(d(M,N))