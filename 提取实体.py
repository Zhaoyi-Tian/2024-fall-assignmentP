def find():
    k=0
    l=list((input().replace("### ###","")).split("### "))
    for i in l:
        if "###" in i:
         k+=1
    return k
n=int(input())
k=0
for i in range(n):
    k+=find()
print(k)
