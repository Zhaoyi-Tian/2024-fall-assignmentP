n=int(input())
words=input().split()
line=[]
current=[]
length=0
for word in words:
    if length+len(word)+(1 if current else 0)>80:
        line.append(current)
        current=[word]
        length=len(word)
    else:
        current.append(str(word))
        length+=len(word)+(1 if current[:-1] else 0)
if current:
    line.append(current)
for i in range(len(line)):
    print(' '.join(line[i]))

