def s(n):
    t=0
    for i in range(n):
        s=1/(i+2)
        t+=s
    return t
def c(c):
    n=1
    while s(n)<c:
        n+=1
    return n
def main():
    while True:
        c_f=float(input())
        if c_f==0.00:
            break
        result=c(c_f)
        print(str(result)+" card(s)")
if __name__=='__main__':
    main()



