from math import log2
def t(n):
    e=(1+n)*n//2
    i=int(log2(n))
    return e-2**(i+2)+2
n=input()
while True:
    try:
        print(t(int(input())))
    except EOFError:
        break











