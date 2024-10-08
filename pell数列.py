def a(n):
    return round((((2+2**0.5)*((1+2**0.5)**(n-1))+(2-2**0.5)*((1-2**0.5)**(n-1))))/4)
n=int(input())
for _ in range(n):
    i=int(input())
    print(a(i)%32767)