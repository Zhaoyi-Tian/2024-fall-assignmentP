n=int(input())
l=map(int,input().split())
c=list(range(1,1000000))
i=1
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n) if is_prime[p]]

# 生成1到1000000之间的所有素数
primes = sieve_of_eratosthenes(1000000)
def find(i):
    return int(i**0.5)==i**0.5
def a(i):
    if not find(i) or i==1:
        return "NO"
    else:
        if i**0.5 in primes:
            return "YES"
        else:
            return "NO"
for i in l:
    print(a(i))