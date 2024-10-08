x=0
def bt(word):
    global x
    word=word.replace("X","")
    if word=="++":
        x+=1
    elif word=="--":
        x-=1
n=int(input())
for i in range(n):
    i=input()
    bt(i)
print(x)