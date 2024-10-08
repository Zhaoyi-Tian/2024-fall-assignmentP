n=int(input())
l=map(int,input().split())
def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return set(prime_numbers)
c=sieve_of_eratosthenes(1000000)
def find(i):
    return int(i**0.5)==i**0.5
def a(i):
    if not find(i) or i==1:
        return "NO"
    else:
        if i**0.5 in c:
            return "YES"
        else:
            return "NO"
for i in l:
    print(a(i))

