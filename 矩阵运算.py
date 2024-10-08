def read():
    row,col=map(int,input().split())
    neirong=[list(map(int,input().split())) for i in range(row)]
    return row,col,neirong
def multiply(A,B):
    result=[[0 for _ in range(len(B[0]))]for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for n in range(len(A[0])):
                result[i][j] += A[i][n]*B[n][j]
    return result
def add(C,D):
    if len(C) != len(D) or len(C[0]) != len(D[0]):
        raise ValueError("Error!")
    result=[[0 for _ in range(len(C[0]))]for _ in range(len(C))]
    for i in range(len(C)):
        for j in range(len(C[0])):
            result[i][j] += C[i][j]+D[i][j]
    return result
ar,ac,A=read()
br,bc,B=read()
cr,cc,C=read()
if ac!=br:
    print("Error!")
elif ar!=cr or bc!=cc:
    print("Error!")
else:
    D=multiply(A,B)
    E=add(C,D)
    for i in range(ar):
       print(' '.join(map(str,E[i])))
