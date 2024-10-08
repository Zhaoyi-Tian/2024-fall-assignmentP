def qiou(a,b,c):
        if b==0:
            b=-b
        if b**2-4*a*c==0:
            d=e=-b/(2*a)
            return f"x1=x2={d:.5f}"
        elif b**2-4*a*c>0:
            d=(-b+(b*b-4*a*c)**0.5)/(2*a)
            e=(-b-(b*b-4*a*c)**0.5)/(2*a)
            if d<e:
                d,e=e,d
            return f"x1={d:.5f};x2={e:.5f}"
        else:
            i=((4*a*c-b**2)**0.5/(2*a))
            d=-b/(2*a)
            return f"x1={d:.5f}+{i:.5f}i;x2={d:.5f}-{i:.5f}i"
n=int(input())
while True:
    try:
        a,b,c=map(float,input().split())
        print(qiou(a,b,c))
    except EOFError:
        break
