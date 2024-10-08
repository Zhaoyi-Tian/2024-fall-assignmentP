import math

def is_prime(n):
    """ 判断n是否为素数 """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_t_prime(x):
    """ 判断x是否为T-prime """
    # 计算x的平方根
    root = int(math.sqrt(x))
    # 检查x是否是完全平方数，并且它的平方根是素数
    return root * root == x and is_prime(root)

# 读取输入
n = int(input())
numbers = list(map(int, input().split()))

# 对每个数进行T-prime判断并输出结果
for num in numbers:
    print("YES" if is_t_prime(num) else "NO")