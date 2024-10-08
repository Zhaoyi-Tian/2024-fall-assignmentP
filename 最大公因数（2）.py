n=int(input())
def y(n):
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
        if i>=6:
            return i
        elif n//i>=6:
            return n//i
  return 1
print(y(n))