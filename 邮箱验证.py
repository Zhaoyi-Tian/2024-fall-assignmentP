def detect(a,b):
    for x,y in enumerate(a):
        if y==b:
            return x
    return -1
while True:
    try:
        a=list(input())
        if a.count("@")!=1:
            m="NO"
        else:
            c=detect(a,"@")
            d=[i for i,char in enumerate(a) if char=="."]
            if c==0 or c==len(a)-1 or (0 in d) or (len(a)-1) in d or c+1 in d or c-1 in d:
                m="NO"
            elif not d or all(pos<c for pos in d):
                m="NO"
            else:
                m="YES"
        print(m)
    except EOFError:
        break


