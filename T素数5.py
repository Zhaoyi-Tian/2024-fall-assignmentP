import math

def sieve_of_eratosthenes(limit):
    """ 使用埃拉托斯特尼筛法生成从2到limit的所有素数 """
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]
    return set(prime_numbers)

# 生成直到sqrt(10^12)的所有素数
primes = sieve_of_eratosthenes(int(math.sqrt(10**12)))

def is_t_prime(x):
    """ 判断x是否为T-prime """
    root = int(math.sqrt(x))
    # 检查x是否是完全平方数，并且它的平方根在素数集合中
    return root * root == x and root in primes

# 读取输入
n = int(input())
numbers = list(map(int, input().split()))

# 对每个数进行T-prime判断并输出结果
for num in numbers:
    print("YES" if is_t_prime(num) else "NO")